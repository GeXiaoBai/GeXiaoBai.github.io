---
title: 使用Cloudflare免费加速Github Pages
---
<div style="margin-top: -2px;"></div>
Github Page 在国内访问速度非常慢，而且图片加载不出来，迫于无奈在网上找到了一个能白嫖加速 Github Page 的办法，就是套一层 Cloudflare CDN，这里记录一下操作步骤。
<hr style="height:2px;border:none;border-top:2px dashed #e6e6fa;">

需要一个域名，可以在阿里云或者华为云购买，也可以在freenom.com注册一个免费的域名。
![](https://www.imgur.la/images/2025/12/29/yuming.png)

注册一个<a href="https://dash.cloudflare.com/login" target="top">Cloudflare</a>账号

<div style="display: flex; justify-content: center;">
    <a class="fancybox fancybox.image" href="https://www.imgur.la/images/2025/12/29/english.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="english" data-caption="english"><img src="https://www.imgur.la/images/2025/12/29/english.png" alt="english" height="30"></a>
    <p>&nbsp;&nbsp;---&gt;&nbsp;&nbsp;</p>
    <a class="fancybox fancybox.image" href="https://www.imgur.la/images/2025/12/29/chinese.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="chinese" data-caption="chinese"><img src="https://www.imgur.la/images/2025/12/29/chinese.png" alt="chinese" height="30"></a>
</div>

注册账号
![](https://www.imgur.la/images/2025/12/29/zhuce.png)
![](https://www.imgur.la/images/2025/12/29/zhuce2.png)

<div style="display: flex; justify-content: center;">
    <p>点击添加站点</p><a class="fancybox fancybox.image" href="https://www.imgur.la/images/2025/12/29/tjzd.png" itemscope="" itemtype="http://schema.org/ImageObject" itemprop="url" data-fancybox="default" rel="default" title="tjzd" data-caption="tjzd"><img src="https://www.imgur.la/images/2025/12/29/tjzd.png" alt="tjzd" height="30"></a>
</div>

![](https://www.imgur.la/images/2025/12/29/ssym.png)
![](https://www.imgur.la/images/2025/12/29/ssym2.png)
打开域名控制台并点击域名
![](https://www.imgur.la/images/2025/12/29/ymkzt.png)
点击修改
![](https://www.imgur.la/images/2025/12/29/dnsxg.png)
然后
![注：DNS服务器的两个为刚才Cloudflare 名称服务器获取的两个NS值](https://www.imgur.la/images/2025/12/29/dnsxg2.png)
点击确定然后在等一会便可