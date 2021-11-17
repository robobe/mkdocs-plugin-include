# mkdocs-plugin-include


## Setup



Activate the plugin in `mkdocs.yml`:
```yaml
plugins:
  - search
  - code_include
```

## Config

* `base_path` - base path to relative reference

> If file path isn't absolute path plugin use this as a base folder

## develop

```
python3 setup.py develop --user
```