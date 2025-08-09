import clsx from 'clsx';
import Heading from '@theme/Heading';
import Translate from '@docusaurus/Translate';
import styles from './styles.module.css';

const FeatureList = [
  {
    titleId: 'homepage.feature1.title',
    descriptionId: 'homepage.feature1.description',
    Svg: require('@site/static/img/immersion.svg').default,
  },
  {
    titleId: 'homepage.feature2.title',
    descriptionId: 'homepage.feature2.description',
    Svg: require('@site/static/img/narrative.svg').default,
  },
  {
    titleId: 'homepage.feature3.title',
    descriptionId: 'homepage.feature3.description',
    Svg: require('@site/static/img/docs.svg').default,
  },
];

function Feature({Svg, titleId, descriptionId}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">
          <Translate id={titleId} />
        </Heading>
        <p>
          <Translate id={descriptionId} />
        </p>
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
