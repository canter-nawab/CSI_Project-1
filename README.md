Contibutors: Bhavesh Kalra, Mayank SIngh Rajkumar, Shivam Kashaudhan


CSI_Project

Telegenic Express

It is a platform for independent film makers and the people who are willing to share videos. Filmmakers can collaborate to provide better content.There is a different account for different user.Account is compulsory for accessing the site.Every user can upload their videos.There is also asearch column for the same.There is acomment section for each video as well as description for it.

Technologies used-django,bootstrap,html,css,js


We have created a file 'posts' in tele_exp/csi.Accessing the link http://127.0.0.1:8000/ will lead you to our home page.Home page contains the posts. There is a button in every post which will lead you to contents of that post and date on which that post was created.You can create any post in this using http://127.0.0.1:8000/create/. You can delete any post using http://127.0.0.1:8000/post_no./delete/. You can edit the post using http://127.0.0.1:8000/post_no./edit/. You can upload the image also. You will get a proper message after performing any of the above operations discussed.

We have created a file 'accounts' in tele_exp/csi.This file contains the basic user's login,logout and signup(register) stuffs which can be accessed by http://127.0.0.1:8000/login, http://127.0.0.1:8000/logout,http://127.0.0.1:8000/register. In it's signup's form we have four fields. If you are already a member of this website then this will not let you create a new account and in this password section,password do not appear when you are typing it.In the register(signup) form we have two email sections,first one is email and second one is confirm email,what this does is if you are entering right password at one place and rewriting it wrong at second place it will show some kind of message. If the user is not in the database,it can not let you login. You will get a welcome message after above operations(like signing up or logging in) discussed.

A file in the tele_exp/csi called Templates contains all the HTML files. A file called media_cdn (tele_exp/csi) contains all uploaded files(images,videos ).

We are working to make a rate button for each video and also a view(no. of views) button for each video . Our website will be having more posts arranged in several rows(like youtube)(using bootstrap) which will lead user to the video.We will implement a search column for searching.We will implement the 'filters' for each section of videos.

