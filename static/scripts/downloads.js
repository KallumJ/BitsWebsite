const masterpageStyle = `background: url("$") no-repeat center center fixed; -webkit-background-size: cover; -moz-background-size: cover; -o-background-size: cover; background-size: cover;`
const imageDir = "../static/assets/images/downloads/"

// Preload images, so theres no white flash
let wd1Img = new Image()
wd1Img.src = imageDir + "112.jpg"

let wd2Img = new Image()
wd2Img.src = imageDir + "113.jpg"

let wd3Img = new Image()
wd3Img.src = imageDir + "114.jpg"

let wd4Img = new Image()
wd4Img.src = imageDir + "116.jpg"

let wd5Img = new Image()
wd5Img.src = imageDir + "117.jpg"

let vResourceImg = new Image()
vResourceImg.src = imageDir + "vanillapack.jpg"

let bResourceImg = new Image()
bResourceImg.src = imageDir + "bitsplus.jpg"

let initalBackgroundImg = new Image()
initalBackgroundImg.src = imageDir + "DownloadsBackground.jpg"


// Store images in array so JS doesnt release them
let images = [wd1Img, wd2Img, wd3Img, vResourceImg, bResourceImg, initalBackgroundImg, wd4Img, wd5Img]

function changeImg(index) {
    document.getElementById("masterpage").style = masterpageStyle.replace("$", images[index].src)
}

function resetImg() {
    changeImg(5)
}

function wd1On() {
    changeImg(0);
}

function wd1Off() {
    resetImg()
}

function wd1Redirect() {
    location.href = "https://download.bits.team/worlds/1.12/"
}

function wd2On() {
    changeImg(1)
}

function wd2Off() {
    resetImg()
}

function wd2Redirect() {
    location.href = "https://download.bits.team/worlds/1.13/"
}

function wd3On() {
    changeImg(2)
}

function wd3Off() {
    resetImg()
}

function wd3Redirect() {
    location.href = "https://download.bits.team/worlds/1.15/"
}

function wd4On() {
    changeImg(6)
}

function wd4Off() {
    resetImg()
}

function wd4Redirect() {
    location.href = "https://download.bits.team/worlds/1.16"
}

function wd5On() {
    changeImg(7)
}

function wd5Off() {
    resetImg()
}

function wd5Redirect() {
    location.href = "https://download.bits.team/worlds/1.17"
}

function vResourceOn() {
    changeImg(3)
}

function vResourceOff() {
    resetImg()
}

function vResourceRedirect() {
    location.href = "https://download.bits.team/resourcepack"
}

function bResourceOn() {
    changeImg(4)
}

function bResourceOff() {
    resetImg()
}

function bResourceRedirect() {
    alert("Bits+ Resource Pack is currently unavailable")
    //location.href = "https://hogwarts.bits.team/resources"
}
