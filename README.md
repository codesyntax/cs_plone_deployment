[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-orange.json)](https://github.com/copier-org/copier)

# Copier template for Plone/Volto deployments

This template is what we use at [CodeSyntax](https://www.codesyntax.com/en) to generate deployment configuration for our Plone/Volto based deployments

## Usage

You first need to have a project created using [cookieplone](https://github.com/plone/cookieplone). It will work both with the _Volto_ and _Classic_ project types.

```bash
uvx cookieplone
```

Then you need to run the following command to get the files in this template:

```bash
cd <your-project-folder>
uvx --with copier-templates-extensions copier copy gh:codesyntax/cs_plone_deployment . --trust
```

And voilà, you will get a `.gitlab-ci.yml` file with the GitLab CI/CD configuration, and a `deploy` folder with the `docker-compose.yml` and all other required configuration files.

In the `deploy` folder you will find a `Makefile` that will help you with your deployments.
