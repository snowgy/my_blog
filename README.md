# my_blog
此个人博客使用django1.10.4和python3.5搭建，前端使用了pure，bootstrap框架。博客实现了评论，站内搜索，归档（按日期），标签分类等功能。博客的后台直接使用了django自带的admin。博客前期根据andrewliu的教程搭建https://github.com/Andrew-liu/my_blog_tutorial  后期自己做了一些修改，实现了一些新的功能。
## Install
```
$ git clone https://github.com/snowgy/my_blog
```
## Usage
```
$ cd my_blog
$ pip install -r requirements.txt 
$ python manage.py migrate
$ python manage.py runserver
注意事项：若电脑上同时装有python2和python3，上述命令中的pip和python应改为pip3和python3.
```
## Shortcomings
1. views.py没有写成类，导致有重复代码段的出现

## To Improve
1. 标签后面需要统计出文章的数量
2. 增加统计博文浏览量功能
