const path = require('path')
const vueLoader = require("vue-loader/lib/plugin")

module.exports = {
    entry: {
        dashboard: "./assets/dashboard.js",
    },
    output: {
        filename: "[name].min.js",
        path: path.resolve(__dirname, 'media/js'),
        publicPath: "./media/js/"
    },
    module: {
        rules: [
            {
                test: /\.css$/,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /\.vue$/,
                loader: "vue-loader"
            },
            {
                test: /\.(eot|svg|ttf|woff|woff2)(\?\S*)?$/,
                use: ['file-loader']
            },
            {
                test: /\.(png|jpe?g|gif|svg)(\?\S*)?$/,
                use: ['file-loader']
            },
            {
              test: /\.s(c|a)ss$/,
              use: [
                'vue-style-loader',
                'css-loader',
                {
                  loader: 'sass-loader',
                  // Requires sass-loader@^7.0.0
                  options: {
                    implementation: require('sass'),
                    fiber: require('fibers'),
                    indentedSyntax: true // optional
                  },
                  // Requires sass-loader@^8.0.0
                  options: {
                    implementation: require('sass'),
                    sassOptions: {
                      fiber: require('fibers'),
                      indentedSyntax: true // optional
                    },
                  },
                },
              ],
            },
        ]
    },
    plugins: [
        new vueLoader()
    ],
    devServer: {

    },
    resolve: {
        alias: {
            "vue": "vue/dist/vue.js"
        }
    },
    mode: 'development'
}
