document.getElementById('change-meme').addEventListener('click', function() {
    const memes = ['meme1.jpg', 'meme2.jpg', 'meme3.jpg'];
    const currentMeme = document.getElementById('meme-image').src;
    const currentIndex = memes.indexOf(currentMeme.split('/').pop());
    const nextIndex = (currentIndex + 1) % memes.length;
    document.getElementById('meme-image').src = memes[nextIndex];
});
