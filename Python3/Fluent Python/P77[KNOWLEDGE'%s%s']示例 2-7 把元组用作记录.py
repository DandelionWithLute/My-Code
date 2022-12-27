lax_coodinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

#❶ 洛杉矶国际机场的经纬度。
#❷ 东京市的一些信息：市名、年份、人口（单位：百万）、人口变化
#（单位：百分比）和面积（单位：平方千米）。
#❸ 一个元组列表，元组的形式为 (country_code,
#passport_number)。
#❹ 在迭代的过程中，passport 变量被绑定到每个元组上。
#❺ % 格式运算符能被匹配到对应的元组元素上。
#❻ for 循环可以分别提取元组里的元素，也叫作拆包（unpacking）。因
#为元组中第二个元素对我们没有什么用，所以它赋值给“_”占位符。
#拆包让元组可以完美地被当作记录来使用，这也是下一节的话题。