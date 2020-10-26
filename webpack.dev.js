const common = require('./webpack.common.js');
const webpack = require('webpack');
const { merge } = require('webpack-merge');
const path = require('path');

module.exports = merge(common, {
    mode: 'development',
    devtool: 'eval-source-map',
    plugins: [
        new webpack.EnvironmentPlugin({
            LOG_LEVEL: 'trace'
        })
    ]
});
