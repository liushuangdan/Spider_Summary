
XPATH
===


上一部分说到正则表达式，正则表达式通常被用来检索，替换那些符合某个模式(规则)的文本。

那么缺点是：
1. 当匹配稍微复杂的时候，很难被理解
1. 正则表达式的性能很难把握。
所以这个时候我们就可以运用j解析数据包。

---

测试的话可以选择下面这个包：

~~~python
pip install lxml
~~~

---
## XPATH 术语介绍

节点(Node)

请看下面这个 XML 文档：

```html
<bookstore>

<book>
  <title lang="en">Harry Potter</title>
  <author>J K. Rowling</author> 
  <year>2005</year>
  <price>29.99</price>
</book>

</bookstore>
```
上面的XML文档中的节点例子：  

```html
<bookstore> （文档节点）
<author>J K. Rowling</author> （元素节点）
lang="en" （属性节点） 
```
基本值的例子：

```html
J K. Rowling
"en"
```
---

#####节点之间的关系
---
**父（Parent）**

每个元素以及属性都有一个父  

在下面的例子中，book 元素是 title、author、year 以及 price 元素的父：

```html
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```
---
**子（Children）**

元素节点可有零个、一个或多个子。  

在下面的例子中，title、author、year 以及 price 元素都是 book 元素的子： 
```html
<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
```
---
**先辈(Ancestor)**   

某节点的父、父的父，等等。  

在下面的例子中，title 元素的先辈是 book 元素和 bookstore 元素： 

```html
<bookstore>

<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

</bookstore>
```
---
**后代（Descendant）**   

某个节点的子，子的子，等等。  

在下面的例子中，bookstore 的后代是 book、title、author、year 以及 price 元素：

```html
<bookstore>

<book>
  <title>Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>

</bookstore>
```
---

### 选取节点
---

```html
<?xml version="1.0" encoding="ISO-8859-1"?>

<bookstore>

<book>
  <title lang="eng">Harry Potter</title>
  <price>29.99</price>
</book>

<book>
  <title lang="eng">Learning XML</title>
  <price>39.95</price>
</book>

</bookstore>
```

|表达式	|描述|
|:------------- |:---------------:|
|nodename|	选取此节点的所有子节点。|
|/	|从根节点选取。|
|//	|从匹配选择的当前节点选择文档中的节点，而不考虑它们的位置。|
|.	|选取当前节点。|
|..|	选取当前节点的父节点。|
|@|	选取属性。|

---
**实例**

在下面的表格中，我们已列出了一些路径表达式以及表达式的结果：

|路径表达式	|结果|
|:------------- |:---------------:|
|bookstore	|选取 bookstore 元素的所有子节点。|
|/bookstore	|选取根元素 bookstore。<br>注释：假如路径起始于正斜杠( / )，则此路径始终代表到某元素的绝对路径！|
|bookstore/book|	选取属于 bookstore 的子元素的所有 book 元素。|
|//book	|选取所有 book 子元素，而不管它们在文档中的位置。|
|bookstore//book|	选择属于 bookstore 元素的后代的所有 book 元素，而不管它们位于 bookstore 之下的什么位置。|
|//@lang|	选取名为 lang 的所有属性。|


**谓语（Predicates）**<br>
谓语用来查找某个特定的节点或者包含某个指定的值的节点。<br>
谓语被嵌在方括号中。<br>
实例: <br>

在下面的表格中，我们列出了带有谓语的一些路径表达式，以及表达式的结果：

|路径表达式	|结果|
|:------------- |:---------------:|
|/bookstore/book[1]	|选取属于 bookstore 子元素的第一个 book 元素。|
|/bookstore/book[last()]	|选取属于 bookstore 子元素的最后一个 book 元素。|
|/bookstore/book[last()-1]	|选取属于 bookstore 子元素的倒数第二个 book 元素。|
|/bookstore/book[position()<3]	|选取最前面的两个属于 bookstore 元素的子元素的 book 元素。|
|//title[@lang]	|选取所有拥有名为 lang 的属性的 title 元素。|
|//title[@lang='eng']|	选取所有 title 元素，且这些元素拥有值为 eng 的 lang 属性。|
|/bookstore/book[price>35.00]|	选取 bookstore 元素的所有 book 元素，且其中的 price 元素的值须大于 35.00。|
|/bookstore/book[price>35.00]/title	|选取 bookstore 元素中的 book 元素的所有 title 元素，且其中的 price 元素的值须大于 35.00。|



