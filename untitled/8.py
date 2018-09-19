import re
html =  """<span class="top_score">7315</span>
        <span class="top_score">7316</span>
        <span class="top_score">73</span>
        <span class="top_score">715</span>
        <span class="top_score">15</span>"""    #多行用三引号
res = re.findall('<span class="top_score">(.+?)</span',html)   #findall寻找html中两个固定部分中间的部分
print(res)
