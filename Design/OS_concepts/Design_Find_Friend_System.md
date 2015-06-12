## POI (Point Of Interest)

### GeoHash
#### Introduction 
* Usage
    * as a unique identifier.
    * represent point data e.g. in databases.
    * 把GeoHash的string做为key，然后该区域的餐馆信息做为value来缓存

* 字符串越长，表示的范围越精确
* 字符串相似的表示距离相近
* 纬度: latitude value, the interval -90 to +90, 经度:longtitude value, -180 to +180

#### [Procudure](http://www.cnblogs.com/LBSer/p/3310455.html)

#### [Disadvantage]((http://en.wikipedia.org/wiki/Geohash)):
* 由于GeoHash是将区域划分为一个个规则矩形，并对每个矩形进行编码，这样在查询附近POI信息时会导致以下问题，
比如红色的点是我们的位置，绿色的两个点分别是附近的两个餐馆，但是在查询的时候会发现距离较远餐馆的GeoHash编码与我们一样
（因为在同一个GeoHash区域块上），而较近餐馆的GeoHash编码与我们不一致。这个问题往往产生在边界处

* 解决的思路很简单，我们查询时，除了使用定位点的GeoHash编码进行匹配外，还使用周围8个区域的GeoHash编码，这样可以避免这个问题。

### Reference
* [POI](http://1.znku.sinaapp.com/?p=331)
* [R tree](http://blog.csdn.net/v_july_v/article/details/6530142#t2)
* [GeoHash wiki page](http://en.wikipedia.org/wiki/Geohash)
* [GeoHash 核心讲解](http://www.cnblogs.com/LBSer/p/3310455.html)
