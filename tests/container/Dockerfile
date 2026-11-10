ARG PYTHON_VERSION=3.12
FROM koalaman/shellcheck:v0.11.0 AS shellcheck

FROM node:24.22.2 AS markdown
WORKDIR /opt/markdown
COPY tests/container/package.json tests/container/package-lock.json ./
RUN npm ci --ignore-scripts --no-audit --no-fund

FROM python:${PYTHON_VERSION}
COPY requirements-dev.txt /opt/check/requirements-dev.txt
RUN python -m venv /opt/venv \
    && /opt/venv/bin/python -m pip install --disable-pip-version-check -r /opt/check/requirements-dev.txt
COPY --from=shellcheck /bin/shellcheck /usr/local/bin/shellcheck
COPY --from=markdown /usr/local/bin/node /usr/local/bin/node
COPY --from=markdown /opt/markdown /opt/markdown
ENV PATH="/opt/markdown/node_modules/.bin:/opt/venv/bin:${PATH}"
COPY tests/container/check /opt/check/run
RUN chmod 755 /opt/check/run
WORKDIR /work
