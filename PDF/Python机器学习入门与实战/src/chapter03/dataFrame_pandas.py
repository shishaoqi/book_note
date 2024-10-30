from pandas import DataFrame

print('利用Pandas模块的DataFrame, 通过字典标记的方式获取Series结构列数据')

paints = {
    "字画名称":["旭日东升","富水长流","招财进宝","鸿运当头"],
    "字画底价":[2860,498,1068,598],
    "字画拍卖加价":[1000,2000,500,1500]
}
goods_in=DataFrame(paints, index=["第一幅","第二幅","第三幅","第四幅"])
paints_price=goods_in["字画底价"]
print(paints_price)


#如果访问的是行，可以通过位置和名称的方式进行获取，代码如下
print('\n利用Pandas模块的DataFrame通过位置获取Series结构行数据')
paints = {
    "字画名称":["旭日东升","富水长流","招财进宝","鸿运当头"],
    "字画底价":[2860,498,1068,598],
    "字画拍卖加价":[1000,2000,500,1500]
}
goods_in=DataFrame(paints,index=["第一幅","第二幅","第三幅","第四幅"])
paints_three=goods_in.loc["第三幅"]
print(paints_three)


print('/n利用Pandas模块的DataFrame通过位置结合切片获取数据')
paints = {
    "字画名称":["旭日东升","富水长流","招财进宝","鸿运当头"],
    "字画底价":[2860,498,1068,598],
    "字画拍卖加价":[1000,2000,500,1500]
}
goods_in = DataFrame(
    paints,
    index=["第一幅","第二幅","第三幅","第四幅"]
)
    
paints_three=goods_in.loc["第三幅":"第四幅","字画名称":"字画底价"]
print(paints_three)
print("---------------------------------------------------")
paints_four=goods_in.loc[["第三幅","第四幅"],["字画名称","字画底价"]]
print(paints_four)


print('/n利用Pandas模块的DataFrame通过位置结合布尔型数组获取数据')
paints={
    "字画名称":["旭日东升","富水长流","招财进宝","鸿运当头"],
    "字画底价":[2860,498,1068,598],
    "字画拍卖加价":[1000,2000,500,1500]
}
goods_in=DataFrame(paints,index=["第一幅","第二幅","第三幅","第四幅"])
paints_three=goods_in.loc[goods_in["字画底价"]>500,:]
print(paints_three)
print("------------------------------------------")
paints_four=goods_in.loc[(goods_in["字画底价"]>500)&(goods_in["字画拍卖加价"]>1000),:]
print(paints_four)