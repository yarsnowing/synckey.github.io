Title: Enable Pelican to Render Markdown Tables
Date: 2017.03.19
Category: tools
Tags: tools,pelican,blog
Slug: enable-pelican-to-render-markdown-tables
Author: Andy
Place: Beijing

Pelican will not process markdown style table in default. However, if you want to use this kind of tables. You can add the follow config to the pelicanconf.py

    :::python
    MARKDOWN = {
        'extension_configs': {
            'markdown.extensions.tables':{},
        }
    }
Then,you can use the following code to generate the table below.

    |First Header  | Second Header|
    |------------- | -------------|
    |Content Cell  | Content Cell|
    |Content Cell  | Content Cell|


|First Header  | Second Header|
|------------- | -------------|
|Content Cell  | Content Cell|
|Content Cell  | Content Cell|


###References

[Markdown extensions](https://pythonhosted.org/Markdown/extensions/tables.html)

