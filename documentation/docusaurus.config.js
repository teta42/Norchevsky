// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  // Title and tagline are defined in i18n JSON files for localization
  // These values serve as fallback for English locale
  title: 'Norchevsky',
  tagline: 'Neuro-game engine for AI adventures',
  favicon: 'img/favicon.ico',

  url: 'https://teta42.github.io',
  baseUrl: '/Norchevsky/',
  trailingSlash: false,

  organizationName: 'teta42',
  projectName: 'Norchevsky',

  onBrokenLinks: 'warn',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'ru',
    locales: ['ru', 'en'],
    localeConfigs: {
      ru: {
        htmlLang: 'ru',
        label: 'Русский',
      },
      en: {
        htmlLang: 'en',
        label: 'English',
      },
    },
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/teta42/Norchevsky/edit/main/',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: 'all',
            xslt: true,
          },
          editUrl: 'https://github.com/teta42/Norchevsky/edit/main/',
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'ignore',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      navbar: {
        // Title is now defined in i18n JSON files
        logo: {
          alt: 'Логотип Норчевского',
          src: 'img/logo.svg',
        },
        items: [
          { to: '/docs/intro', label: 'Документация', position: 'left' },
          { to: '/blog', label: 'Блог', position: 'left' },
          { href: 'https://github.com/teta42/Norchevsky', label: 'GitHub', position: 'right' },
          {
            type: 'localeDropdown',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [],
        copyright:
          `© ${new Date().getFullYear()} Norchevsky. Все права защищены.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

module.exports = config;
