# 导入

from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

# 准备数据
lst=[['华为',1000],['apple',3000],['Xiaomi',980],['Samsung',2300]]


c = (
    Pie()
#    .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .add('',lst)
    .set_global_opts(title_opts=opts.TitleOpts(title="2024 phone sell number"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("phone.html")
)
