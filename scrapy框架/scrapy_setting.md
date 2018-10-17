## scrapy内置设置参考 setting 

以下是所有可用Scrapy设置的列表，按字母顺序，以及其默认值和适用范围。

范围（如果可用）显示设置在哪里使用，如果它绑定到任何特定组件。在这种情况下，将显示该组件的模块，通常是扩展，中间件或管道。这也意味着必须启用组件才能使设置具有任何效果。

### AWS_ACCESS_KEY_ID

默认： `None`

由需要访问[Amazon Web服务](https://aws.amazon.com/)的代码使用的AWS访问密钥，例如[S3源存储后端](https://doc.scrapy.org/en/1.3/topics/feed-exports.html#topics-feed-storage-s3)。

### AWS_SECRET_ACCESS_KEY

默认： `None`

由需要访问Amazon Web服务的代码使用的AWS密钥，例如S3源存储后端。

### BOT_NAME

默认： `'scrapybot'`

此Scrapy项目实施的bot的名称（也称为项目名称）。这将用于默认情况下构造User-Agent，也用于日志记录。

当您使用`startproject`命令创建项目时，它会自动填充您的项目名称。

### CONCURRENT_ITEMS

默认： `100`

在项处理器（也称为[项目管道](https://doc.scrapy.org/en/1.3/topics/item-pipeline.html#topics-item-pipeline)）中并行处理的并发项目的最大数量（每个响应）。

### CONCURRENT_REQUESTS

默认： `16`

将由Scrapy下载程序执行的并发（即同时）请求的最大数量。

### CONCURRENT_REQUESTS_PER_DOMAIN

默认： `8`

将对任何单个域执行的并发（即同时）请求的最大数量。

参见：[AutoThrottle扩展](https://doc.scrapy.org/en/1.3/topics/autothrottle.html#topics-autothrottle)及其 `AUTOTHROTTLE_TARGET_CONCURRENCY`选项。

### CONCURRENT_REQUESTS_PER_IP

默认： `0`

将对任何单个IP执行的并发（即同时）请求的最大数量。如果非零，`CONCURRENT_REQUESTS_PER_DOMAIN`则忽略该 设置，而改为使用此设置。换句话说，并发限制将应用于每个IP，而不是每个域。

此设置也会影响`DOWNLOAD_DELAY`和 [AutoThrottle扩展](https://doc.scrapy.org/en/1.3/topics/autothrottle.html#topics-autothrottle)：如果`CONCURRENT_REQUESTS_PER_IP` 非零，下载延迟是强制每IP，而不是每个域。

### DEFAULT_ITEM_CLASS

默认： `'scrapy.item.Item'`

将用于[在Scrapy shell](https://doc.scrapy.org/en/1.3/topics/shell.html#topics-shell)中实例化项的默认类。

### DEFAULT_REQUEST_HEADERS

默认：

```
{
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
}1234
```

用于Scrapy HTTP请求的默认标头。他们居住在 `DefaultHeadersMiddleware`。

### DEPTH_LIMIT

默认： `0`

范围： `scrapy.spidermiddlewares.depth.DepthMiddleware`

允许抓取任何网站的最大深度。如果为零，则不施加限制。

### DEPTH_PRIORITY

默认： `0`

范围： `scrapy.spidermiddlewares.depth.DepthMiddleware`

用于根据深度调整请求优先级的整数：

如果为零（默认），则不从深度进行优先级调整 
正值将降低优先级，即，较高深度请求将被稍后处理 ; 这通常用于做广度优先爬网（BFO） 
负值将增加优先级，即，较高深度请求将被更快地处理（DFO） 
参见：[Scrapy是否以广度优先或深度优先顺序爬行？](https://doc.scrapy.org/en/1.3/faq.html#faq-bfo-dfo)关于调整BFO或DFO的Scrapy。

#### 注意

此设置以与其他优先级设置 和相反的方式调整优先级。`REDIRECT_PRIORITY_ADJUSTRETRY_PRIORITY_ADJUST`

### DEPTH_STATS

默认： True

范围： `scrapy.spidermiddlewares.depth.DepthMiddleware`

是否收集最大深度统计。

### DEPTH_STATS_VERBOSE

默认： `False`

范围： `scrapy.spidermiddlewares.depth.DepthMiddleware`

是否收集详细的深度统计信息。如果启用此选项，则在统计信息中收集每个深度的请求数。

### DNSCACHE_ENABLED

默认： `True`

是否启用DNS内存缓存。

### DNSCACHE_SIZE

默认： `10000`

DNS内存缓存大小。

### DNS_TIMEOUT

默认： `60`

以秒为单位处理DNS查询的超时。支持浮点。

### DOWNLOADER

默认： `'scrapy.core.downloader.Downloader'`

用于抓取的下载器。

### DOWNLOADER_HTTPCLIENTFACTORY

默认： `'scrapy.core.downloader.webclient.ScrapyHTTPClientFactory'`

定义`protocol.ClientFactory` 用于HTTP / 1.0连接（for `HTTP10DownloadHandler`）的`Twisted` 类。

#### 注意

HTTP / 1.0现在很少使用，所以你可以安全地忽略这个设置，除非你使用Twisted <11.1，或者如果你真的想使用HTTP / 1.0和覆盖`DOWNLOAD_HANDLERS_BASE`相应的`http(s)`方案，即到 `'scrapy.core.downloader.handlers.http.HTTP10DownloadHandler'`。

### DOWNLOADER_CLIENTCONTEXTFACTORY

默认： `'scrapy.core.downloader.contextfactory.ScrapyClientContextFactory'`

表示要使用的`ContextFactory`的类路径。

这里，“ContextFactory”是用于SSL / TLS上下文的Twisted术语，定义要使用的TLS / SSL协议版本，是否执行证书验证，或者甚至启用客户端验证（以及各种其他事情）。

#### 注意

Scrapy默认上下文工厂**不执行远程服务器证书验证**。这通常对于网络刮削是很好的。

如果您需要启用远程服务器证书验证，Scrapy还有另一个上下文工厂类，您可以设置， `'scrapy.core.downloader.contextfactory.BrowserLikeContextFactory'`使用平台的证书来验证远程端点。 **仅当使用Twisted> = 14.0时，此选项才可用**。

如果你使用一个自定义的ContextFactory，确保它接受一个`method` 参数在init（这是`OpenSSL.SSL`方法映射`DOWNLOADER_CLIENT_TLS_METHOD`）。

### DOWNLOADER_CLIENT_TLS_METHOD

默认： `'TLS'`

使用此设置可自定义默认HTTP / 1.1下载程序使用的TLS / SSL方法。

此设置必须是以下字符串值之一：

- `'TLS'`：映射到OpenSSL `TLS_method()`（aka `SSLv23_method()`），允许协议协商，从平台支持的最高开始; 默认，推荐
- `'TLSv1.0'`：此值强制HTTPS连接使用TLS版本1.0; 如果你想要Scrapy <1.1的行为，设置这个
- `'TLSv1.1'`：强制TLS版本1.1
- `'TLSv1.2'`：强制TLS版本1.2
- `'SSLv3'`：强制SSL版本3**（不推荐）**

#### 注意

我们建议您使用PyOpenSSL> = 0.13和Twisted> = 0.13或以上（如果可以，Twisted> = 14.0）。

### DOWNLOADER_MIDDLEWARES

默认：： `{}`

包含在您的项目中启用的下载器中间件及其顺序的字典。有关更多信息，请参阅激活下载器中间件。

### DOWNLOADER_MIDDLEWARES_BASE

默认：

```
{
    'scrapy.downloadermiddlewares.robotstxt.RobotsTxtMiddleware': 100,
    'scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware': 300,
    'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware': 350,
    'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware': 400,
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': 500,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': 550,
    'scrapy.downloadermiddlewares.ajaxcrawl.AjaxCrawlMiddleware': 560,
    'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware': 580,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 590,
    'scrapy.downloadermiddlewares.redirect.RedirectMiddleware': 600,
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': 700,
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 750,
    'scrapy.downloadermiddlewares.stats.DownloaderStats': 850,
    'scrapy.downloadermiddlewares.httpcache.HttpCacheMiddleware': 900,
}12345678910111213141516
```

包含Scrapy中默认启用的下载器中间件的字典。低订单更靠近发动机，高订单更接近下载器。您不应该在项目中修改此设置，`DOWNLOADER_MIDDLEWARES`而应修改 。有关更多信息，请参阅 [激活下载器中间件](https://doc.scrapy.org/en/1.3/topics/downloader-middleware.html#topics-downloader-middleware-setting)。

### DOWNLOADER_STATS

默认： `True`

是否启用下载器统计信息收集。

### DOWNLOAD_DELAY

默认： `0`

下载器在从同一网站下载连续页面之前应等待的时间（以秒为单位）。这可以用于限制爬行速度，以避免击中服务器太难。支持小数。例：

```
DOWNLOAD_DELAY = 0.25    # 250 ms of delay1
```

此设置也受`RANDOMIZE_DOWNLOAD_DELAY` 设置（默认情况下启用）的影响。默认情况下，Scrapy不会在请求之间等待固定的时间量，而是使用0.5 * `DOWNLOAD_DELAY`和1.5 * 之间的随机间隔`DOWNLOAD_DELAY`。

当`CONCURRENT_REQUESTS_PER_IP`为非零时，每个IP地址而不是每个域强制执行延迟。

您还可以通过设置`download_delay` spider属性来更改每个爬虫的此设置。

### DOWNLOAD_HANDLERS

默认： `{}`

包含在您的项目中启用的请求下载器处理程序的dict。参见`DOWNLOAD_HANDLERS_BASE`示例格式。

### DOWNLOAD_HANDLERS_BASE

默认：

```
{ 
    'file' ： 'scrapy.core.downloader.handlers.file.FileDownloadHandler' ，
    'http' ： 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler' ，
    'https' ： 'scrapy.core.downloader.handlers。 http.HTTPDownloadHandler' ，
    's3' ： 'scrapy.core.downloader.handlers.s3.S3DownloadHandler' ，
    'ftp' ： 'scrapy.core.downloader.handlers.ftp.FTPDownloadHandler' ，
}1234567
```

包含Scrapy中默认启用的请求下载处理程序的字典。您不应该在项目中修改此设置，`DOWNLOAD_HANDLERS`而应修改 。

您可以通过在其中`None`分配URI方案来禁用这些下载处理程序`DOWNLOAD_HANDLERS`。例如，要禁用内置的FTP处理程序（无替换），请将其放置在`settings.py`：

```
DOWNLOAD_HANDLERS = {
    'ftp': None,
}123
```

### DOWNLOAD_TIMEOUT

默认： `180`

下载器在超时前等待的时间量（以秒为单位）。

#### 注意

可以使用`download_timeout` Spider属性和每个请求使用`download_timeout` `Request.meta`键为每个爬虫设置此超时。

### DOWNLOAD_MAXSIZE

默认值：`1073741824（1024MB）`

下载器将下载的最大响应大小（以字节为单位）。

如果要禁用它设置为0。

#### 注意

可以使用`download_maxsize` Spider属性和每个请求使用`download_maxsize` Request.meta键为每个爬虫设置此大小。

此功能需要Twisted> = 11.1。

### DOWNLOAD_WARNSIZE

默认值：33554432（32MB）

下载程序将开始警告的响应大小（以字节为单位）。

如果要禁用它设置为0。

#### 注意

可以使用`download_warnsize` Spider属性和每个请求使用`download_warnsize` Request.meta键为每个爬虫设置此大小。

此功能需要Twisted> = 11.1。

### DUPEFILTER_CLASS

默认： `'scrapy.dupefilters.RFPDupeFilter'`

用于检测和过滤重复请求的类。

默认（RFPDupeFilter）过滤器基于请求指纹使用该`scrapy.utils.request.request_fingerprint`函数。为了改变重复检查的方式，你可以子类化`RFPDupeFilter`并重载它的`request_fingerprint`方法。这个方法应该接受scrapy `Request`对象并返回其指纹（一个字符串）。

### DUPEFILTER_DEBUG

默认： `False`

默认情况下，`RFPDupeFilter`只记录第一个重复的请求。设置`DUPEFILTER_DEBUG`为`True`将使其记录所有重复的请求。

### EDITOR

默认值：取决于环境

用于使用edit命令编辑爬虫的编辑器。它默认为EDITOR环境变量，如果设置。否则，它默认为vi（在Unix系统上）或IDLE编辑器（在Windows上）。

### EXTENSIONS

默认：： `{}`

包含项目中启用的扩展名及其顺序的字典。

### EXTENSIONS_BASE

默认：

```
{
    'scrapy.extensions.corestats.CoreStats': 0,
    'scrapy.extensions.telnet.TelnetConsole': 0,
    'scrapy.extensions.memusage.MemoryUsage': 0,
    'scrapy.extensions.memdebug.MemoryDebugger': 0,
    'scrapy.extensions.closespider.CloseSpider': 0,
    'scrapy.extensions.feedexport.FeedExporter': 0,
    'scrapy.extensions.logstats.LogStats': 0,
    'scrapy.extensions.spiderstate.SpiderState': 0,
    'scrapy.extensions.throttle.AutoThrottle': 0,
}1234567891011
```

包含默认情况下在Scrapy中可用的扩展名及其顺序的字典。此设置包含所有稳定的内置扩展。请记住，其中一些需要通过设置启用。

有关详细信息，请参阅[扩展程序用户指南](https://doc.scrapy.org/en/1.3/topics/extensions.html#topics-extensions) 和[可用扩展列表](https://doc.scrapy.org/en/1.3/topics/extensions.html#topics-extensions-ref)。

### FEED_TEMPDIR

Feed Temd dir允许您在使用[FTP源存储](https://doc.scrapy.org/en/1.3/topics/feed-exports.html#topics-feed-storage-ftp)和 Amazon S3上传之前设置自定义文件夹以保存搜寻器临时文件。

### ITEM_PIPELINES

默认： `{}`

包含要使用的项目管道及其顺序的字典。顺序值是任意的，但通常将它们定义在0-1000范围内。较低订单处理较高订单前。

例：

```
ITEM_PIPELINES = {
    'mybot.pipelines.validate.ValidateMyItem': 300,
    'mybot.pipelines.validate.StoreMyItem': 800,
}1234
```

### ITEM_PIPELINES_BASE

默认： `{}`

包含Scrapy中默认启用的管道的字典。您不应该在项目中修改此设置，`ITEM_PIPELINES`而应修改。

### LOG_ENABLED

默认： `True`

是否启用日志记录。

### LOG_ENCODING

默认： `'utf-8'`

用于记录的编码。

### LOG_FILE

默认： `None`

用于记录输出的文件名。如果None，将使用标准误差。

### LOG_FORMAT

默认： `'%(asctime)s [%(name)s] %(levelname)s: %(message)s'`

用于格式化日志消息的字符串。有关[可用占位符](https://docs.python.org/2/library/logging.html#logrecord-attributes)的完整列表，请参阅[Python日志记录](https://docs.python.org/2/library/logging.html#logrecord-attributes)文档。

### LOG_DATEFORMAT

默认： `'%Y-%m-%d %H:%M:%S'`

用于格式化日期/时间的字符串，占位符的%(asctime)s扩展`LOG_FORMAT`。有关[可用指令](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior)的完整列表，请参阅[Python datetime](https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior)文档。

### LOG_LEVEL

默认： `'DEBUG'`

记录的最低级别。可用级别为：`CRITICAL`，`ERROR`，`WARNING`，`INFO`，`DEBUG`。有关详细信息，请参阅日志。

### LOG_STDOUT

默认： `False`

如果`True`，您的进程的所有标准输出（和错误）将被重定向到日志。例如，如果它将出现在Scrapy日志中。`print 'hello'`

### LOG_SHORT_NAMES

默认： `False`

如果`True`，日志将仅包含根路径。如果设置为，`False` 则它显示负责日志输出的组件

### MEMDEBUG_ENABLED

默认： `False`

是否启用内存调试。

### MEMDEBUG_NOTIFY

默认： `[]`

当启用内存调试时，如果此设置不为空，则会将内存报告发送到指定的地址，否则报告将写入日志。

例：

```
MEMDEBUG_NOTIFY = ['user@example.com']1
```

### MEMUSAGE_ENABLED

默认： `False`

范围： `scrapy.extensions.memusage`

是否启用内存使用扩展，当超过内存限制时关闭Scrapy进程，并在发生这种情况时通过电子邮件通知。

请参阅内存使用扩展。

### MEMUSAGE_LIMIT_MB

默认： `0`

范围： `scrapy.extensions.memusage`

在关闭Scrapy之前允许的最大内存量（以兆字节为单位）（如果`MEMUSAGE_ENABLED`为`True`）。如果为零，则不执行检查。

请参阅[内存使用扩展](https://doc.scrapy.org/en/1.3/topics/extensions.html#topics-extensions-ref-memusage)。

### MEMUSAGE_CHECK_INTERVAL_SECONDS

新版本1.1。

默认： `60.0`

范围： `scrapy.extensions.memusage`

该[内存使用扩展](https://doc.scrapy.org/en/1.3/topics/extensions.html#topics-extensions-ref-memusage) 检查当前内存使用情况，相对于限制由设置 `MEMUSAGE_LIMIT_MB`和`MEMUSAGE_WARNING_MB`在固定的时间间隔。

这将设置这些间隔的长度（以秒为单位）。

请参阅[内存使用扩展](https://doc.scrapy.org/en/1.3/topics/extensions.html#topics-extensions-ref-memusage)。

### MEMUSAGE_NOTIFY_MAIL

默认： `False`

范围： `scrapy.extensions.memusage`

要达到内存限制时通知的电子邮件列表。

例：

```
MEMUSAGE_NOTIFY_MAIL = ['user@example.com']1
```

请参阅[内存使用扩展](https://doc.scrapy.org/en/1.3/topics/extensions.html#topics-extensions-ref-memusage)。

### MEMUSAGE_REPORT

默认： `False`

范围： `scrapy.extensions.memusage`

是否在每个爬虫关闭后发送内存使用报告。

请参阅内存使用扩展。

### MEMUSAGE_WARNING_MB

默认： `0`

范围： `scrapy.extensions.memusage`

在发送警告电子邮件通知之前，要允许的最大内存量（以兆字节为单位）。如果为零，则不会产生警告。

### NEWSPIDER_MODULE

默认： `''`

模块在哪里使用`genspider`命令创建新的爬虫。

例：

```
NEWSPIDER_MODULE = 'mybot.spiders_dev'1
```

### RANDOMIZE_DOWNLOAD_DELAY

默认： `True`

如果启用，Scrapy会在从同一网站获取请求时等待随机时间（介于0.5 * `DOWNLOAD_DELAY`和1.5 *之间`DOWNLOAD_DELAY`）。

该随机化降低了由分析请求的站点检测（并随后阻塞）爬行器的机会，所述站点在它们的请求之间的时间内寻找统计上显着的相似性。

随机化策略与wget –random-wait选项使用的策略相同。

如果`DOWNLOAD_DELAY`为零（默认），此选项不起作用。

### REACTOR_THREADPOOL_MAXSIZE

默认： `10`

Twisted Reactor线程池大小的上限。这是各种Scrapy组件使用的常见多用途线程池。线程DNS解析器，BlockingFeedStorage，S3FilesStore仅举几个例子。如果您遇到阻塞IO不足的问题，请增加此值。

### REDIRECT_MAX_TIMES

默认： 20

定义请求可重定向的最长时间。在此最大值之后，请求的响应被原样返回。我们对同一个任务使用Firefox默认值。

### REDIRECT_PRIORITY_ADJUST

默认： +2

范围： scrapy.downloadermiddlewares.redirect.RedirectMiddleware

相对于原始请求调整重定向请求优先级：

- 正优先级调整（默认）意味着更高的优先级。
- 负优先级调整意味着较低优先级。

### RETRY_PRIORITY_ADJUST

默认： `-1`

范围： `scrapy.downloadermiddlewares.retry.RetryMiddleware`

调整相对于原始请求的重试请求优先级：

- 正优先级调整意味着更高的优先级。
- 负优先级调整（默认）表示较低优先级。

### ROBOTSTXT_OBEY

默认： `False`

范围： `scrapy.downloadermiddlewares.robotstxt`

如果启用，Scrapy会尊重robots.txt政策。有关详细信息，请参阅 [RobotsTxtMiddleware](https://doc.scrapy.org/en/1.3/topics/downloader-middleware.html#topics-dlmw-robots)。

#### 注意

虽然默认值是`False`由于历史原因，默认情况下在settings.py文件中通过命令生成此选项。`scrapy startproject`

### SCHEDULER

默认： `'scrapy.core.scheduler.Scheduler'`

用于爬网的调度程序。

### SCHEDULER_DEBUG

默认： `False`

设置True将记录有关请求调度程序的调试信息。如果请求无法序列化到磁盘，则当前日志（仅一次）。Stats counter（`scheduler/unserializable`）跟踪发生的次数。

日志中的示例条目：

```
1956-01-31 00:00:00+0800 [scrapy.core.scheduler] ERROR: Unable to serialize request:
<GET http://example.com> - reason: cannot serialize <Request at 0x9a7c7ec>
(type Request)> - no more unserializable requests will be logged
(see 'scheduler/unserializable' stats counter)1234
```

### SCHEDULER_DISK_QUEUE

默认： `'scrapy.squeues.PickleLifoDiskQueue'`

将由调度程序使用的磁盘队列的类型。其它可用的类型有 `scrapy.squeues.PickleFifoDiskQueue`，`scrapy.squeues.MarshalFifoDiskQueue`， `scrapy.squeues.MarshalLifoDiskQueue`。

### SCHEDULER_MEMORY_QUEUE

默认： `'scrapy.squeues.LifoMemoryQueue'`

调度程序使用的内存中队列的类型。其他可用类型是： `scrapy.squeues.FifoMemoryQueue`。

### SCHEDULER_PRIORITY_QUEUE

默认： `'queuelib.PriorityQueue'`

调度程序使用的优先级队列的类型。

### SPIDER_CONTRACTS

默认：： `{}`

包含在项目中启用的爬虫契约的dict，用于测试爬虫。有关更多信息，请参阅[爬虫合同](https://doc.scrapy.org/en/1.3/topics/contracts.html#topics-contracts)。

### SPIDER_CONTRACTS_BASE

默认：

```
{
    'scrapy.contracts.default.UrlContract' : 1,
    'scrapy.contracts.default.ReturnsContract': 2,
    'scrapy.contracts.default.ScrapesContract': 3,
}12345
```

包含Scrapy中默认启用的scrapy合约的dict。您不应该在项目中修改此设置，SPIDER_CONTRACTS 而应修改。有关更多信息，请参阅[爬虫合同](https://doc.scrapy.org/en/1.3/topics/contracts.html#topics-contracts)。

您可以通过`None`将其中的类路径指定为禁用任何这些合同`SPIDER_CONTRACTS`。例如，要禁用内置 `ScrapesContract`，将此放在您的`settings.py`：

```
SPIDER_CONTRACTS = {
    'scrapy.contracts.default.ScrapesContract': None,
}123
```

### SPIDER_LOADER_CLASS

默认： `'scrapy.spiderloader.SpiderLoader'`

将用于加载爬虫程序的类，它必须实现 [SpiderLoader API](https://doc.scrapy.org/en/1.3/topics/api.html#topics-api-spiderloader)。

### SPIDER_LOADER_WARN_ONLY

新版本1.3.3。

默认： `False`

默认情况下，当scrapy尝试从中导入爬虫类时`SPIDER_MODULES`，如果有任何`ImportError`异常，它将大声失败。但是你可以选择沉默此异常，并通过设置将其变成一个简单的警告。`SPIDER_LOADER_WARN_ONLY = True`

#### 注意

有些scrapy命令使用此设置运行`True` 已经（即他们只会发出警告并不会失败），因为他们实际上并不需要加载爬虫类的工作: `scrapy runspider`, `scrapy settings`, `scrapy startproject`, `scrapy version`.

### SPIDER_MIDDLEWARES

默认：： {}

包含在您的项目中启用的爬虫中间件的字典及其顺序。有关更多信息，请参阅激活爬虫中间件。

### SPIDER_MIDDLEWARES_BASE

默认：

```
{
    'scrapy.spidermiddlewares.httperror.HttpErrorMiddleware': 50,
    'scrapy.spidermiddlewares.offsite.OffsiteMiddleware': 500,
    'scrapy.spidermiddlewares.referer.RefererMiddleware': 700,
    'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware': 800,
    'scrapy.spidermiddlewares.depth.DepthMiddleware': 900,
}1234567
```

包含在Scrapy中默认启用的爬虫中间件的字典及其顺序。低订单更靠近发动机，高订单更接近爬虫。有关更多信息，请参阅激活爬虫中间件。

SPIDER_MODULES 
默认： []

Scrapy将寻找爬虫的模块列表。

例：

```
SPIDER_MODULES = ['mybot.spiders_prod', 'mybot.spiders_dev']1
```

### STATS_CLASS

默认： `'scrapy.statscollectors.MemoryStatsCollector'`

用于收集统计信息的类，谁必须实现 [Stats Collector API](https://doc.scrapy.org/en/1.3/topics/api.html#topics-api-stats)。

STATS_DUMP 
默认： True

一旦爬虫完成，转储[Scrapy统计](https://doc.scrapy.org/en/1.3/topics/stats.html#topics-stats)（到Scrapy日志）。

更多信息请参阅：[统计数据收集](https://doc.scrapy.org/en/1.3/topics/stats.html#topics-stats)。

### STATSMAILER_RCPTS

默认:( `[]`空列表）

爬虫完成刮擦后发送Scrapy stats。查看 StatsMailer更多信息。

### TELNETCONSOLE_ENABLED

默认： `True`

布尔值，指定是否 启用[telnet控制台](https://doc.scrapy.org/en/1.3/topics/telnetconsole.html#topics-telnetconsole)（如果其扩展名也启用）。

### TELNETCONSOLE_PORT

默认： `[6023, 6073]`

用于telnet控制台的端口范围。如果设置为None或0，则使用动态分配的端口。有关详细信息，请参阅 [telnet控制台](https://doc.scrapy.org/en/1.3/topics/telnetconsole.html#topics-telnetconsole)。

### TEMPLATES_DIR

默认值：`templates` dir里面的scrapy模块

使用`startproject`命令和新爬虫创建新项目时使用命令查找模板的目录 `genspider` 。

项目名称不得与子目录中的自定义文件或目录的名称冲突`project`。

### URLLENGTH_LIMIT

默认： `2083`

范围： `spidermiddlewares.urllength`

允许抓取网址的最大网址长度。有关此设置的默认值的详细信息，请参阅<http://www.boutell.com/newfaq/misc/urllength.html>

### USER_AGENT

默认： `"Scrapy/VERSION (+http://scrapy.org)"`

检索时使用的默认用户代理，除非被覆盖。