
常用的css选择器
===

| 选择器                                                       | 例子             | 例子描述                                         | CSS  |
| ------------------------------------------------------------ | ---------------- | ------------------------------------------------ | ---- |
| .*class*                                                     | .intro           | 选择 class="intro" 的所有元素。                  | 1    |
| #*id*                                                        | #firstname       | 选择 id="firstname" 的所有元素。                 | 1    |
| *                                                            | *                | 选择所有元素。                                   | 2    |
| *element*                                                    | p                | 选择所有 <p> 元素。                              | 1    |
| *element*,*element*                                          | div,p            | 选择所有 <div> 元素和所有 <p> 元素。             | 1    |
| *element* *element*                                          | div p            | 选择 <div> 元素内部的所有 <p> 元素。             | 1    |
| *element*>*element*                                          | div>p            | 选择父元素为 <div> 元素的所有 <p> 元素。         | 2    |
| *element*+*element*                                          | div+p            | 选择紧接在 <div> 元素之后的所有 <p> 元素。       | 2    |
| [*attribute*\]                                               | [target]         | 选择带有 target 属性所有元素。                   | 2    |
| [*attribute*=*value*\]                                       | [target=_blank]  | 选择 target="_blank" 的所有元素。                | 2    |
| [*attribute*~=*value*\]                                      | [title~=flower]  | 选择 title 属性包含单词 "flower" 的所有元素。    | 2    |
| [*attribute*\|=*value*\]                                     | [lang\|=en]      | 选择 lang 属性值以 "en" 开头的所有元素。         | 2    |
| [:nth-of-type(*n*)](http://www.w3school.com.cn/cssref/selector_nth-of-type.asp) | p:nth-of-type(2) | 选择属于其父元素第二个 <p> 元素的每个 <p> 元素。 | 3    |


