# Usage

 - provide a `data/secret.yaml` file that contains a `secret` key with the API key to Grafana
 - run `make image`
 - run `make convert` to convert the files in the in directory to the out directory
 - run `make apply` to update Grafana's dashboards.

## Format of data/secret.yaml

```yaml
secret: blahblah
```

## Configurations

The `data/setup.yaml` configuration file contains about the API endpoint that
this tool will be writing to along with some other properties such as the
datasource for the respective dashboard.

The files inside the `in` directory are the input files that are transformed
through the src/convert.py script, resulting to the generation of the
transformed versions of these files in the `out` directory. Feel free to mutate
this the convert script to make further changes as necessary.
