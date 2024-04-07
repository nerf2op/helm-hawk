Control all your operations with helm-hawk!
===========================================

Introduction
------------

Wrapper CLI build on top helm cli . This CLI provides you with a set of commands to manage your resources. You can use the following commands:

*  **diff**:       Group of commands for comparing two versions of helm chart
*  **get**:        Group of commands to retrieve information from the server
*  **history**:    Commands related to the history of changes in a project.
*  **list**:       This command lists all of the releases for a specified...
*  **pull**:       Retrieve a package from a package repository, and download...
*  **repo**:       This command consists of multiple subcommands to interact...
*  **rollback**:   This command rolls back a release to a previous revision.
*  **status**:     This command shows the status of a named release.
*  **template**:   Render chart templates locally and display the output
*  **uninstall**:  This command takes a release name and uninstalls the release.
*  **upgrade**:    This command upgrades a release to a new version of a chart.
    

Global Options
------------


*   **\--context (-c)**: Specify the name of the context you want to use
    
*   **\--namespace (-n)**: Indicate the namespace for which you want to see the resources
    

Requirements
------------

[Helm3](https://helm.sh/docs/intro/install/) \
[Kubectl](https://kubernetes.io/docs/tasks/tools/#kubectl)



## Installation

Install `helm-hawk` using pip:

```bash
pip install helm-hawk
```

## Usage

```bash
helm-hawk [OPTIONS] COMMAND [ARGS]...
```

### Options

- `-c, --context`: Name of the context you want to use
- `-n, --namespace`: Namespace for which you want to see the resources.
- `--help`: Show this message and exit.

### Commands

#### `diff`

Group of commands for comparing two versions of Helm chart

```bash
helm-hawk diff [OPTIONS] COMMAND [ARGS]...
```

##### Options

- `--help`: Show this message and exit.

##### Commands

- `revision`: Show a diff of a specific revision against the last known one.
- `upgrade`: Show a diff explaining what a Helm upgrade would change.

#### `get`

Group of commands to retrieve information from the server

```bash
helm-hawk get [OPTIONS] COMMAND [ARGS]...
```

##### Options

- `--help`: Show this message and exit.

##### Commands

- `values`: Fetches values for a specific release

#### `history`

Commands related to the history of changes in a project.

```bash
helm-hawk history [OPTIONS] RELEASE_NAME
```

##### Options

- `--max INTEGER`: Maximum number of revisions to include in history (default 256)
- `-c, --context TEXT`: Context that you want to use
- `-n, --namespace TEXT`: Namespace you want to use
- `--help`: Show this message and exit.

#### `list`

This command lists all of the releases for a specified namespace (uses current namespace context if namespace not specified).

```bash
helm-hawk list [OPTIONS]
```
##### Options

- `-a, --all`: Show all releases without any filter applie (default 256)
- `-A, --all-namespaces`: List releases across all namespaces
- `-n, --namespace TEXT`: Namespace you want to use
- `--help`: Show this message and exit.

#### `pull`

Retrieve a package from a package repository, and download it locally.
```bash
helm-hawk pull [OPTIONS] CHART_NAME
```
##### Options:

- `--version TEXT`: specify a version constraint for the chart version to use. This constraint can be a specific tag (e.g. 1.1.1) or it may reference a valid range (e.g. ^2.0.0). If this is not specified, the latest version is used
- `--username TEXT`: chart repository username where to locate the requested chart
- `--password TEXT`: chart repository password where to locate the requested chart
- `--untar`: if set to true, will untar the chart after downloading it
- `--repo TEXT`: chart repository url where to locate the requested chart
- `--pass-credentials`: pass credentials to all domains
- `--help`: Show this message and exit.


#### `repo`

This command consists of multiple subcommands to interact with chart
  repositories.

```bash
helm-hawk repo [OPTIONS] COMMAND [ARGS]...
```

##### Options

- `--help`: Show this message and exit.

##### Commands

- `add`: Add a chart repository
- `list`: List chart repositories
- `remove`: Remove one or more chart repositories
- `update`: Update gets the latest information about charts

#### `rollback`

This command rolls back a release to a previous revision.

```bash
helm-hawk rollback [OPTIONS] RELEASE_NAME REVISION
```

##### Options

- `-c, --context TEXT`: Context that you want to use
- `-n, --namespace TEXT`: Namespace you want to use
- `--dry-run`: Simulate a rollback
- `--no-hooks`: Prevent hooks from running during rollback
- `--help`: Show this message and exit.

#### `status`

This command shows the status of a named release.

```bash
helm-hawk status [OPTIONS] RELEASE_NAME
```

##### Options

- `-c, --context TEXT`: Context that you want to use
- `-n, --namespace TEXT`: Namespace you want to use
- `--revision TEXT`: If set, display the status of the named release with revision
- `-o, --output TEXT`: Prints the output in the specified format. Allowed values: table, json, yaml (default table)
- `--show-desc`: If set, display the description message of the named release
- `--help`: Show this message and exit.

#### `template`

Render chart templates locally and display the output

```bash
helm-hawk template [OPTIONS] RELEASE_NAME CHART_PATH
```

##### Options

- `-c, --context TEXT`: Context that you want to use
- `-n, --namespace TEXT`: Namespace you want to use
- ` -f, --values TEXT `: Specify values in a YAML file (can specify multiple)
release
- `--help`: Show this message and exit.

#### `uninstall`

This command takes a release name and uninstalls the release.

```bash
helm-hawk uninstall [OPTIONS] RELEASE_NAME
```

##### Options

- `-c, --context TEXT`: Context that you want to use
- `-n, --namespace TEXT`: Namespace you want to use
- `--dry-run`: Simulate the upgrade
- `--help`: Show this message and exit.

#### `upgrade`

This command upgrades a release to a new version of a chart.

```bash
helm-hawk upgrade [OPTIONS] RELEASE_NAME CHART_PATH
```

##### Options

- `-f, --values TEXT`: Specify values in a YAML file (can specify multiple)
- `-c, --context TEXT`: Context that you want to use
- `-n, --namespace TEXT`: Namespace you want to use
- `--dry-run`: Simulate the upgrade
- `--help`: Show this message and exit.
