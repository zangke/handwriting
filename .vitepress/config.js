module.exports = {
  title: '书法',
  description: '书法日日学',
  head: createHead(),
  themeConfig: {
    logo: '/logo.png',
    lastUpdated: false,
    repo: 'zangke/handwriting',
    docsBranch: 'dev',
    editLinks: false,
    nav: createNav(),
    sidebar: createSidebar(),
  },
};

function createHead() {
  return [
    ['meta', {
      name: 'author',
      content: 'zangke168@foxmail.com'
    }],
    [
      'meta',
      {
        name: 'viewport',
        content: 'width=device-width,initial-scale=1,minimum-scale=1.0,maximum-scale=1.0,user-scalable=no',
      },
    ],
    ['meta', {
      name: 'keywords',
      content: 'vitepress handwriting 书法 字帖'
    }],
    ['link', {
      rel: 'icon',
      href: '/favicon.ico'
    }],
    [
      'script',
      {
        src: 'https://code.jquery.com/jquery-3.3.1.min.js',
      },
    ],
    [
      'script',
      {
        src: 'https://cdn.bootcdn.net/ajax/libs/fancybox/3.5.7/jquery.fancybox.min.js',
      },
    ],
    [
      'link',
      {
        rel: 'stylesheet',
        type: 'text/css',
        href: 'https://cdn.bootcdn.net/ajax/libs/fancybox/3.5.7/jquery.fancybox.min.css',
      },
    ],
  ];
}

function createNav() {
  return [{
      text: '首页',
      link: '/',
    },
    {
      text: '书家',
      link: '/shujia/',
    },
    {
      text: '字帖',
      link: '/zitie/',
    },
    {
      text: '知识',
      link: '/zhishi/',
    },
    {
      text: '日记',
      link: '/notes/',
    },
  ];
}

function createSidebar() {
  return {
    '/shujia/': [{
      text: '书家',
      children: [{
          text: '王羲之',
          link: '/shujia/wangxizhi',
        },
        {
          text: '王献之',
          link: '/shujia/wangxianzhi',
        },
        {
          text: '虞世南',
          link: '/shujia/yushinan',
        },
        {
          text: '欧阳询',
          link: '/shujia/ouyangxun',
        },
        {
          text: '颜真卿',
          link: '/shujia/yanzhenqing',
        },
        {
          text: '苏东坡',
          link: '/shujia/sudongpo',
        },
        {
          text: '黄庭坚',
          link: '/shujia/huangtingjan',
        },
        {
          text: '米芾',
          link: '/shujia/mifu',
        },
      ],
    }, ],
    '/zitie/': [{
      text: '字帖',
      children: [{
          text: '兰亭序',
          link: '/zitie/ltx',
        },
        {
          text: '圣教序',
          link: '/zitie/sjx',
        },
        {
          text: '祭侄稿',
          link: '/zitie/jizhigao',
        },
        {
          text: '寒食帖',
          link: '/zitie/hanshitie',
        },
        {
          text: '丘师墓志',
          link: '/zitie/qiushimuzhi',
        },
        {
          text: '苏轼《归去来兮辞》',
          link: '/zitie/sdp_gqlxc',
        },
        {
          text: '赵孟頫《归去来兮辞》',
          link: '/zitie/zmf_gqlxc',
        },
        {
          text: '蔡京行书《王希孟千里江山图跋》',
          link: '/zitie/cj_qljstb',
        },
        {
          text: '蔡京行书《跋宋徽宗唐十八学士图卷》',
          link: '/zitie/cj_sbxst',
        },
        {
          text: '蔡京行书送郝玄明使秦一首',
          link: '/zitie/cj_shxm',
        },
        {
          text: '蔡京《题赵佶听琴图》',
          link: '/zitie/cj_zjtqt',
        },
        {
          text: '冯志福岳阳楼记行书字帖',
          link: '/zitie/xs_yylj',
        },
        {
          text: '杨凝式神仙笔法临摹',
          link: '/zitie/yns_sxbf',
        },
      ],
    }, ],
    '/zhishi/': [{
      text: '知识',
    }, ],
    '/notes/': [{
      text: '日记',
    }, ],
    '/': [{
      text: '首页',
      children: [{
        text: '其他',
        link: '/other/',
      }, ],
    }, ],
  };
}