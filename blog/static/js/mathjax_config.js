MathJax.Hub.Config({
    showProcessingMessages: false, //关闭js加载过程信息
    messageStyle: "none", //不显示信息
    extensions: ["tex2jax.js"],
    jax: ["input/TeX", "output/HTML-CSS"],
    tex2jax: {
        inlineMath: [['$', '$'], ["\\(", "\\)"]],
        displayMath: [['$$', '$$'], ["\\[", "\\]"]],
        skipTags: ['h1', 'h2', 'h3', 'h4', 'h5'],
    },
    'HTML-CSS': {
        linebreaks: {automatic: true},
        availableFonts: ["STIX", "TeX"],    // 可选字体
        showMathMenu: false //禁用右键菜单
    }
});
MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
