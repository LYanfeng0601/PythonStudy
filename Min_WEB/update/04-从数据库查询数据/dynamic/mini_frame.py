import re
from pymysql import connect

"""
URL_FUNC_DICT = {
    "/index.html": index,
    "/center.html": center
}
"""

URL_FUNC_DICT = dict()


def route(url):
    def set_func(func):
        # URL_FUNC_DICT["/index.py"] = index
        URL_FUNC_DICT[url] = func

        def call_func(*args, **kwargs):
            return func(*args, **kwargs)
        return call_func
    return set_func


@route("/index.html")
def index():
    with open("./templates/index.html") as f:
        content = f.read()

    # my_stock_info = "哈哈哈哈 这是你的本月名称....."
    # content = re.sub(r"\{%content%\}", my_stock_info, content)
    # 创建Connection连接
    conn = connect(host='192.168.0.103', port=3306, user='root',
                   password='root', database='mysql', charset='utf8')
    # 获得Cursor对象
    cs = conn.cursor()
    cs.execute("select * from user;")
    stock_infos = cs.fetchall()
    cs.close()
    conn.close()

    str_template = """
        <tr >
            <td> %s </td>
            <td> %s </td>
            <td> %s </td>
            <td> %s </td>
            <td> %s </td>
            <td> %s </td>
            <td> 0.88 </td>
            <td> %s</td>
            <td>
                <input type="button" value="添加" id="add" systemidvaule='00007'> 
            </td>
        < / tr >
    """
    html = ''
    for line_info in stock_infos:
        html += str_template % (line_info[0], line_info[1], line_info[2], line_info[
                                3], line_info[4], line_info[5], line_info[6], line_info[7])

    content = re.sub(r"\{%content%\}", str(html), content)

    return content


@route("/center.html")
def center():
    with open("./templates/center.html") as f:
        content = f.read()

    my_stock_info = "这里是从mysql查询出来的数据。。。"

    content = re.sub(r"\{%content%\}", my_stock_info, content)

    return content


def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])

    file_name = env['PATH_INFO']
    # file_name = "/index.py"

    """
    if file_name == "/index.py":
        return index()
    elif file_name == "/center.py":
        return center()
    else:
        return 'Hello World! 我爱你中国....'
    """

    try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        return URL_FUNC_DICT[file_name]()
    except Exception as ret:
        return "产生了异常：%s" % str(ret)
