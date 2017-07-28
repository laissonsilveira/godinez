"use strict"

const gulp = require('gulp');
const babelify = require('babelify');
const browserify = require('browserify');
const source = require('vinyl-source-stream');
const buffer = require('vinyl-buffer');
const rename = require('gulp-rename');
const gutil = require('gulp-util');

const config = {
  src :'src',
  dest : 'dist'
};

gulp.task('bundle-app', () => {
    browserify(config.src, {debug: true})
      .transform(babelify, {presets: ['es2015']})
      .bundle()
      .pipe(source('bundled-app.js'))
      .pipe(buffer())
      .pipe(rename('app.js'))
      .pipe(gulp.dest(config.dest));
});

gulp.task('watch', () => {
  gulp.watch(config.src + '/**/*.js', ['bundle-app']);
});

gulp.task('build', ['bundle-app']);
gulp.task('build-dev', ['bundle-app','watch'],() => {
  gutil.log(gutil.colors.green('Watch is running...'));
});