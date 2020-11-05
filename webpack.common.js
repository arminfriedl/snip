const { CleanWebpackPlugin } = require('clean-webpack-plugin');
const path = require('path');
const autoprefixer = require('autoprefixer');

module.exports = {
    entry: {
        index: './snip/templates/index.js',
        success: './snip/templates/success.js'
    },
    plugins: [
        new CleanWebpackPlugin()
    ],
    output: {
        filename: '[name].bundle.js',
        path: path.resolve(__dirname, 'snip', 'static', 'dist')
    },
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: [
                    // Creates `style` nodes from JS strings
                    'style-loader',
                    // Translates CSS into CommonJS
                    'css-loader',
                    // - runs autoprefixer
                    // - must come after css/style-loader but before other preprocessors
                    // - webpack evaluates right to left/bottom to top
                    // - Browser compatibility list determined by https://get.foundation/sites/docs/sass.html
                    {loader: 'postcss-loader',
                     options: { postcssOptions:
                                { plugins:
                                  ['postcss-preset-env', { 'browsers': ['last 2 versions', 'ie >= 9', 'android >= 4.4', 'ios >= 7']}]}}}
                ]
            },
            {
                test: /\.s[ac]ss$/i,
                use: [
                    // Creates `style` nodes from JS strings
                    'style-loader',
                    // Translates CSS into CommonJS
                    'css-loader',
                    // - runs autoprefixer
                    // - must come after css/style-loader but before other preprocessors
                    // - webpack evaluates right to left/bottom to top
                    // - Browser compatibility list determined by https://get.foundation/sites/docs/sass.html
                    {loader: 'postcss-loader',
                     options: { postcssOptions:
                                { plugins:
                                  ['postcss-preset-env', {'browsers': ['last 2 versions', 'ie >= 9', 'android >= 4.4', 'ios >= 7']}]}}},
                    // Compiles Sass to CSS
                    'sass-loader',
                ]
            }]
    }
};
