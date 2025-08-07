import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';
// #TODO поменять svg с пустышек на нормальные фото
const FeatureList = [
  {
    title: 'Иммерсивный и интерактивный процесс',
    Svg: require('@site/static/img/immersion.svg').default,
    description: (
      <>
        Норчевский — это не просто движок для игр, а система, в которой вы погружаетесь в живой, реагирующий на вас мир. Каждый ход игрока влияет на историю, создавая настоящую интерактивную симфонию.
      </>
    ),
  },
  {
    title: 'Наратив, рождающийся из мира',
    Svg: require('@site/static/img/narrative.svg').default,
    description: (
      <>
        В отличие от выдуманных сценариев, в Норчевском лор вырастает прямо из мира, из событий, из действий игроков и агентов. История развивается органично, на основе уже существующего контекста.
      </>
    ),
  },
  {
    title: 'Полная документация',
    Svg: require('@site/static/img/docs.svg').default,
    description: (
      <>
        Документация проекта написана с вниманием к деталям и простотой для читателя. Она охватывает архитектуру, примеры, идеи и будущее системы, делая вход в проект понятным и вдохновляющим.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
