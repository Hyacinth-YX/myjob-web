module.exports = {
  publicPath: "./",
  pluginOptions: {
    quasar: {
      importStrategy: "kebab",
      rtlSupport: true,
    },
  },
  transpileDependencies: ["quasar"],
  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:5000/",
        changeOrigin: true,
        ws: true,
        pathRewrite: {
          "^/api": "", // rewrite path
        },
      },
    },
  },
};
