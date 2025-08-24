import os
import yaml
import time
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.callbacks import BaseCallbackHandler

# Загрузка конфигурации из YAML
def load_config(config_path: str) -> dict:
    """
    Загружает конфигурацию из YAML-файла.

    Параметры:
        config_path (str): Путь к файлу конфигурации

    Возвращает:
        dict: Словарь с настройками

    Исключения:
        FileNotFoundError: Если файл конфигурации не найден
        yaml.YAMLError: При ошибке парсинга YAML
    """
    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Конфигурационный файл не найден: {config_path}") from e
    except yaml.YAMLError as e:
        raise ValueError(f"Ошибка парсинга YAML в файле {config_path}: {e}") from e

# Загрузка промта из файла
def load_prompt(prompt_path: str) -> str:
    """
    Загружает содержимое промт-файла.

    Параметры:
        prompt_path (str): Путь к файлу с промтом

    Возвращает:
        str: Содержимое файла

    Исключения:
        FileNotFoundError: Если файл не найден
    """
    try:
        with open(prompt_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Файл промта не найден: {prompt_path}") from e

# Инициализация LLM с настройками из конфига
def initialize_chat_llm(config: dict) -> ChatOpenAI:
    """
    Инициализирует модель OpenAI с настройками для OpenRouter.

    Параметры:
        config (dict): Конфигурация модели

    Возвращает:
        OpenAI: Инициализированный экземпляр LLM

    Исключения:
        ValueError: Если отсутствуют обязательные параметры
    """
    model_settings = config.get('model_settings', {})
    required_keys = ['model_name', 'temperature', 'max_tokens']
    
    if not all(key in model_settings for key in required_keys):
        raise ValueError(f"В конфигурации отсутствуют обязательные ключи модели: {required_keys}")
    
    # Получение API ключа из переменных окружения
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY не найден в переменных окружения")
    
    # OpenRouter требует указания источника запроса в заголовках
    headers = {
        "HTTP-Referer": "https://github.com/teta42/Norchevsky",
        "X-Title": "Norchevsky-Test"
    }
    
    return ChatOpenAI(
        api_key=api_key,
        model=model_settings['model_name'],
        temperature=model_settings['temperature'],
        max_tokens=model_settings['max_tokens'],
        openai_api_base="https://openrouter.ai/api/v1",
        default_headers=headers
    )

# Основная функция обработки цепи
def process_story_chain(user_query: str, config_path: str = "config.yaml") -> str:
    """
    Обрабатывает полную цепь генерации истории с использованием Runnable.

    Параметры:
        user_query (str): Пользовательский запрос
        config_path (str): Путь к файлу конфигурации

    Возвращает:
        str: Сгенерированная история

    Исключения:
        Exception: Любые ошибки в процессе выполнения
    """

    
    # Функция для логирования этапа
    def log_stage(stage_name, input_data, output_data, elapsed_sec):
        print(f"\n{'='*50}")
        print(f"### Этап: {stage_name}")
        print(f"{'-'*50}")
        print("Входные данные (сокращённо):")
        print(str(input_data)[:100] + ("..." if len(str(input_data)) > 100 else ""))
        print(f"\nВыходные данные:")
        print(str(output_data))
        print(f"\nВремя выполнения: {elapsed_sec:.3f} сек")
        print(f"{'='*50}\n")
    
    try:
        # Определяем базовый путь к папке с промтами
        base_prompts_path = os.path.join(os.path.dirname(__file__), "prompts")
        
        # Загрузка промтов
        context_prompt = load_prompt(os.path.join(base_prompts_path, "context_generation.txt"))
        scenarios_prompt = load_prompt(os.path.join(base_prompts_path, "scenario_generation.txt"))
        selection_prompt = load_prompt(os.path.join(base_prompts_path, "scenario_selection.txt"))
        story_prompt = load_prompt(os.path.join(base_prompts_path, "story_generation.txt"))
        
        # Загрузка конфигурации модели
        config = load_config(config_path)
        
        # Инициализация LLM
        llm = initialize_chat_llm(config)
        
        # Общее время начала генерации
        total_start_time = time.perf_counter()
        
        # Создаем этапы с загруженными промтами
        context_generation = (
            {"user_query": RunnablePassthrough()}
            | ChatPromptTemplate.from_messages([
                ("system", context_prompt),
                ("user", "Запрос: {user_query}\n\nКонтекст:")
            ])
            | llm
            | {"context": StrOutputParser()}
        )
        
        scenarios_generation = (
            {"context": RunnablePassthrough()}
            | ChatPromptTemplate.from_messages([
                ("system", scenarios_prompt),
                ("user", "Контекст: {context}\n\nВарианты развития событий:")
            ])
            | llm
            | {"scenarios": StrOutputParser()}
        )
        
        scenario_selection = (
            {"scenarios": RunnablePassthrough()}
            | ChatPromptTemplate.from_messages([
                ("system", selection_prompt),
                ("user", "Варианты:\n{scenarios}\n\nОптимальный вариант:")
            ])
            | llm
            | {"selected_scenario": StrOutputParser()}
        )
        
        story_generation = (
            {"selected_scenario": RunnablePassthrough()}
            | ChatPromptTemplate.from_messages([
                ("system", story_prompt),
                ("user", "Вариант: {selected_scenario}\n\nЗавершенная история:")
            ])
            | llm
            | StrOutputParser()
        )
        
        # Выполняем этапы с замерами времени
        start_time = time.perf_counter()
        context = context_generation.invoke(user_query)
        elapsed = time.perf_counter() - start_time
        log_stage("Генерация контекста", user_query, context['context'], elapsed)
        
        start_time = time.perf_counter()
        scenarios = scenarios_generation.invoke(context)
        elapsed = time.perf_counter() - start_time
        log_stage("Генерация сценариев", context['context'], scenarios['scenarios'], elapsed)
        
        start_time = time.perf_counter()
        selected_scenario = scenario_selection.invoke(scenarios)
        elapsed = time.perf_counter() - start_time
        log_stage("Выбор сценария", scenarios['scenarios'], selected_scenario['selected_scenario'], elapsed)
        
        start_time = time.perf_counter()
        story = story_generation.invoke(selected_scenario)
        elapsed = time.perf_counter() - start_time
        log_stage("Генерация истории", selected_scenario['selected_scenario'], story, elapsed)
        
        # Вычисляем общее время
        total_elapsed = time.perf_counter() - total_start_time
        print(f"\nОбщее время генерации: {total_elapsed:.3f} сек")
        
        return story
    
    except Exception as e:
        # Логирование ошибки с контекстом
        print(f"Ошибка при обработке цепи: {str(e)}")
        raise

# Сохранение результата в файл
def save_story(story: str, output_path: str = "output_story.txt") -> None:
    """
    Сохраняет сгенерированную историю в текстовый файл.

    Параметры:
        story (str): Текст истории
        output_path (str): Путь для сохранения файла

    Исключения:
        IOError: При ошибке записи в файл
    """
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(story)
        print(f"История сохранена в {output_path}")
    except IOError as e:
        print(f"Ошибка при сохранении истории: {str(e)}")
        raise
if __name__ == "__main__":
    # Загрузка переменных окружения
    load_dotenv()
    
    
    # Пример пользовательского запроса
    user_query = "История о путешествии во времени в древний Египет"
    
    try:
        # Обработка цепи
        story = process_story_chain(user_query)
        
        # Сохранение результата
        save_story(story)
        
    except Exception as e:
        print(f"Критическая ошибка: {str(e)}")