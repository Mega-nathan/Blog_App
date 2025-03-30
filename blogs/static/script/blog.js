const add=document.querySelector('.add-button');
const list=document.querySelector('.list-button');
const create=document.querySelector('.create-blog');
const blog_list=document.querySelector('.blog-lists');        
add.addEventListener('click',function(){
    blog_list.classList.add('hidden');
    create.classList.remove('hidden');
});
list.addEventListener('click',function(){
    blog_list.classList.remove('hidden');
    create.classList.add('hidden');
});
document.querySelector('.blog--edit').addEventListener('click',function(){
    console.log('Clicked');
    console.log(window.location);
});
