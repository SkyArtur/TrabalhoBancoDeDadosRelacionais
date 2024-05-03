const {src, dest, watch, series} = require("gulp")
const concat = require("gulp-concat")
const babel = require("gulp-babel")
const uglify = require("gulp-uglify")
const sourcemaps = require("gulp-sourcemaps")
const sass = require("gulp-sass")(require('sass'))


function minifyCss() {
    return src('./src/sass/**/*.sass')
        .pipe(sourcemaps.init())
        .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
        .pipe(concat("style.min.css"))
        .pipe(sourcemaps.write('.'))
        .pipe(dest('./public/css/'))
}

function minifyJs() {
    return src('./src/js/**/*.js')
        .pipe(sourcemaps.init())
        .pipe(babel({presets: ['@babel/preset-env']}))
        .pipe(uglify())
        .pipe(concat("main.min.js"))
        .pipe(sourcemaps.write('.'))
        .pipe(dest('./public/js/'))
}

exports.default = function (){
    watch("./src/sass/main.sass", minifyCss)
    watch("./src/js/**/*.js", minifyJs)
}