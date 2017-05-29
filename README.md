# PythonHW04-KNN（最近鄰居法）
##完成項目
 * 資料前處理(輸出一個txt檔)
 * (K-NN)找出2015/01/01,龍潭的5個鄰居
 * (K-NN)找輸入資料k個最近鄰居
 
##程式說明與截圖

本程式分為三個部份分別對應三個.py檔
分別是 ==preprocessing.py==， ==knn_1.py==，==knn_2.py==
==preprocessing.py== 對輸入檔進行處理，先將缺失值與錯誤值替代成==np.NaN==
並輸出到==buffer.txt==，在讀入==buffer.txt==將NaN替代為平均值
最後輸出==output.txt==

![](https://github.com/miyuiki/PythonHW04-KNN/blob/master/capture/capture%2005292103.jpg?raw=true)

上圖是buffer.txt
下圖是output.txt

![](https://github.com/miyuiki/PythonHW04-KNN/blob/master/capture/capture%2005292104.jpg?raw=true)

第二部分和第三部分則是讀入處理過的==output.txt==
利用歐式距離與相似度計算兩向量間的相似性
最後輸出指定地點的k個鄰居

![](https://github.com/miyuiki/PythonHW04-KNN/blob/master/capture/%E8%9E%A2%E5%B9%95%E5%BF%AB%E7%85%A7%202017-05-29%20%E4%B8%8B%E5%8D%885.06.49.png?raw=true)

