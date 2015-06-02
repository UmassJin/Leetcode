##### 1. Bloom Filter算法:
* 创建一个m位BitSet，先将所有位初始化为0，然后选择k个不同的哈希函数。第i个哈希函数对字符串str哈希的结果记为h（i，str），
且h（i，str）的范围是0到m-1 。

##### 1) 加入字符串过程
* 下面是每个字符串处理的过程，首先是将字符串str“记录”到BitSet中的过程：
* 对于字符串str，分别计算h（1，str），h（2，str）…… h（k，str）。然后将BitSet的第h（1，str）、h（2，str）…… h（k，str）位设为1。

##### 2) 检查字符串是否存在的过程
* 下面是检查字符串str是否被BitSet记录过的过程：
* 对于字符串str，分别计算h（1，str），h（2，str）…… h（k，str）。然后检查BitSet的第h（1，str）、h（2，str）…… h（k，str）位是否为1，若其中任何一位不为1则可以判定str一定没有被记录过。若全部位都是1，则“认为”字符串str存在。
* 若一个字符串对应的Bit不全为1，则可以肯定该字符串一定没有被Bloom Filter记录过。（这是显然的，因为字符串被记录过，其对应的二进制位肯定全部被设为1了）
* 但是若一个字符串对应的Bit全为1，实际上是不能100%的肯定该字符串被Bloom Filter记录过的。（因为有可能该字符串的所有位都刚好是被其他字符串所对应）这种将该字符串划分错的情况，称为false positive 。

##### 3) 删除字符串过程
* 字符串加入了就被不能删除了，因为删除会影响到其他字符串。实在需要删除字符串的可以使用Counting bloomfilter(CBF)，这是一种基本Bloom Filter的变体，CBF将基本Bloom Filter每一个Bit改为一个计数器，这样就可以实现删除字符串的功能了。
* Bloom Filter跟单哈希函数Bit-Map不同之处在于：Bloom Filter使用了k个哈希函数，每个字符串跟k个bit对应。从而降低了冲突的概率。

##### 2. Bloom Filter参数选择
* 1) 哈希函数的个数k、位数组大小m、加入的字符串数量n的关系
* 2) 当hash函数个数k=(ln2)*(m/n)时错误率最小。
* 3) 在错误率不大于E的情况 下，m至少要等于n*lg(1/E)才能表示任意n个元素的集合。但m还应该更大些，因为还要保证bit数组里至少一半为0，
*    则m应 该>=nlg(1/E)*lge 大概就是nlg(1/E)1.44倍(lg表示以2为底的对数)。 

##### Reference 
* http://blog.csdn.net/v_july_v/article/details/6685894
* http://www.dbafree.net/?p=36
