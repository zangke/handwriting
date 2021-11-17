module.exports = {
  title: "书法",
  description: "书法日日学",
  head: [
    [
      "script",
      {
        src: "https://code.jquery.com/jquery-3.3.1.min.js",
      },
    ],
    [
      "script",
      {
        src: "https://cdn.bootcdn.net/ajax/libs/fancybox/3.5.7/jquery.fancybox.min.js",
      },
    ],
    [
      "link",
      {
        rel: "stylesheet",
        type: "text/css",
        href: "https://cdn.bootcdn.net/ajax/libs/fancybox/3.5.7/jquery.fancybox.min.css",
      },
    ],
  ],
  themeConfig: {
    logo: "/logo.png",
    // 头部导航
    nav: [
      {
        text: "首页",
        link: "/",
      },
      {
        text: "日记",
        link: "/notes/",
      },
    ],
    // 侧边导航
    sidebar: {
      "/": [
        { text: "简介", link: "/" },
        { text: "书家", link: "/shujia/" },
        { text: "字帖", link: "/zitie/" },
        { text: "知识", link: "/zhishi/" },
        { text: "日记", link: "/notes/" },
        { text: "其他", link: "/other/" },
      ],
    },
    search: true,
    lastUpdated: false,
    repo: "zangke/handwriting",
    docsDir: "docs",
    docsBranch: "dev",
    editLinks: false,
  },
};
