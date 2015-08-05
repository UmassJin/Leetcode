##关于面试

####1. 准备面试的tips
##### 1) Reach Out to Recruiters
a) Search with a query like recruiter *@adobe.com
* For example: [top 25 recuriter at FB](https://www.linkedin.com/title/recruiter-at-facebook)
b) Alumni Network 

##### 2) Prepare the resume 

####2. 跳槽目的:
1. I have learned a lot and enjoyed working with currect team recently, but I have joined the Cisco for almost three years and participate in design and develop the 2 generation productions in Nexus 7k, right now, we almost focus on the maintaince of the productions, so I want to try the differnt opportunity outside the Cisco. 
2. I want to build my experience in a new industry, I’m interested in working at [name of employer] based on the great things I have learned about it. 
3. Instead of the network area, I want to learn the distributed systems technology, how to build the large systems...*** is the leader in this industry, so working here would mean that I would be at the top of my field. 
4. I really believe that the most important thing for any job is to make sure that you’re learning a lot. Whereas at many companies you really learn only about your own team, at Facebook/Google, employees seem to be encouraged to transfer teams, to share knowledge across teams, to do tech talks about their team’s architecture,

I feel confident that I can leverage my academic, professional, and “extracurricular” experience with
software development to make an impact on Google.

####3. 工作类型:
1. Have participated in design and develop two generations in Nexus 7k products, focus on the L2/L3 features on different generations for forwarding ASICs. 
2. Designed and developed a classic binary logs parsing application using Python, HTML, CSS, jQuery and Javascript. The application used internally in Cisco for debug purpose, more than 1k usages in first 3 months.
3. Designed and developed Virtual Network Segmentation in forwarding infrastructure for NXOS VINCI architecture solution on fabricpath technology

####4. 工作内容:

| Projects | Flanker(F3) | Vinci | Blogger | 
| --- | --- | --- | --- | 
| Most Challenging | details of different traffic flow | Learn the high-level structure, scale issue |  Scale, speed up| 
| What You Learned | traffic flows | IaaS| build website |
| Influencing Someone | new product | next generation data center | QA in data center | 
| Improvement | speed up the component time | improve the scale, reduce the driver calls etc. | 1) more random input 2) add the timestamp, component filter | 
| Mistake |  | | | 

##### Vinci 
1. Current data center architectures are unable to meet growing customer needs in terms of scale, service, flexibility, managebility 
2. Cisco’s solution and strategy is “Vinci” – a next gen data center architecture for scalable multi-tenant data centers – initially targeting Service Provider and Enterprise Data Center segments.  
3. Multi Tenancy is a critical technology in cloud computing. One instance of application can serve multiple customers by sharing the resources. Important technology for N7K to move towards virtualization. Implemented on Vinci architecture with Spine-Leaf topology 
4. Vinci provides a next-generation data center architecture that is built on a spine-leaf topology that provides optimal connectivity at Layer-2 and Layer-3 between hosts at the leaf switches in the fabric and between the hosts and the external network. The fabric essentially provides an overlay network that allows the spine nodes to act as transit nodes that only switch on the fabric overlay header. 

##### Blogger
1. Based on the Pyramid framework 
  * Pyramid uses the WSGI protocol to connect an application and a web server together. 
  * WSGI: Web Server Gateway Interface. This is a Python standard for connecting web applications to web servers, 
    similar to the concept of Java Servlets. Pyramid requires that your application be served as a WSGI application.
  * Pyramid uses the WebOb package as a basis for its request and response object implementations.
  * One of the primary jobs of Pyramid is to find and invoke a view callable when a request reaches your application. 
    View callables are bits of code which do something interesting in response to a request made to your application. 

2. template:
  * Pyramid provides templating via the Chameleon and Mako templating libraries, I use the Mako as template in the frontend for     HTML, css and javascript. 
  * Use 960 Grid system: The 960 Grid System is an effort to streamline web development workflow by providing commonly used        dimensions

3. Process:
1). Extract the input file, create the unique random number("randomID") for each session,
    create a dictionary for each session to save information of each file,such as filename,
    extract_file_path, unique file_ID and time duration of session...
    return the extract result to extract_root.mak

2). check the input file path by user, if the file path does not exists, or user enter
    the blank file path, or iParse can not access the path, raise the exception
    otherwise, process the user input path. 
    
3). Create the randomID for each session. Initialize the Tree() and corresponding
    dictionary. Open a debug file and record the user input file path, randomID,  
    file_path after saved in the /blogger/iparse/tmp, file_ID and filename
    Note: for the server 8081, random number range is (100001,20000)
    for the server 8080, random number range is (1,100000)
    
4). Initialize the Tree: 
    When insert the new children nodes into the tree, first 
    make the pointer point to it's parent node, then insert the children list,
    after insertion, set the pointer to the root node;

    If the parent id is 0,the children id is 0.1,0.2,0.3...
    the children id of node 0.1 is 0.1.1, 0.1.2, 0.1.3....
    Node_fromID() function could find the specific node from the input node ID,
    using the depth first searching, if exists, return the Node object, if not exists, return NULL
    Class Node:
    Each node save the file name, id, parent file and children directories

5).  Copy the input file into "/blogger/iparse/tmp" directory, 
   and save the new path as the file extract 
   path after copy successfully, check the input file type 
   (.tar/gz/zip file or directory), using the 
   corresponding method to extract the input file

6). 
```python
# Two types of user input: If user enter the .tar file path,
# could contain the compressed file and directory 
# If user enter the directory file path, should not contain 
# the compressed files, restrict to scripts
# or directories only; For the compressed files, saved into 
# /blogger/iparse/tmp, for the directory file, use
# the original input path
```

7).
```python
# Extract all the subfiles when user click the directory name
# Extract the compressed file or open the directory when user click the link of filename
# Parse the script file and print the result in the screen when user click the script 
# filename
# Extract the specific component files when user using the search component box
#
# "component"is the name of search input box. 
# "subcomp" is the name of submit button for search input box. 
# First check whether user click the directory and prefer to parse all the subfiles,
# if so, extract all the comporessed subfiles, and then parse the subfiles.
# Second, check whether user enter the component name in search box and submit. 
# If so, extract all the files under the current file path and then parse all the 
# files related with the specific component. 
# iParse also give the search hint to users. If user search the components which 
# are not exist in database, raise the exception. 
# If user use search box and extract the file at the same time, raise the exception. 
# Otherwise, print the parse result in the screen.
```

8). for the normal path, we could get the dir_ID and transfer into the file path
but one more concern is when user enter into the subdirectory and then return back
to the first one, it my has the issue. 
```python
# If user enter into the subdirectory(example:0.5.1.1.1),do not parse the file and 
# return back to the former one (for example: 0.5),system only save the 
# subdirectory fileID (0.5.1.1.1). At this time, when user use the search box, 
# we need to get the fileID (0.5) rather than 0.5.1.1.1. 
# So first check the 'process' value in the current page, if it's not NULL, 
# get the value 0.5.1,(the value of 'process' in each page only record the 
# recent one, such as in the page 0.5, if we extract 0.5.1, in this page, 
# the value of 'process' only record '0.5.1' rather then '0.5.1.1.1'), 
# then using getParent() get the parent node 0.5. 
#
# If user enter into this directory at the first time  and use the search bar 
# directly just get the file_path from directory
```

9). one scenario is, in the input files, if there is already the tree parse include, 
we will not ask the user to enter the tree path again

10). also for each users, has save one file, which has the timestamp, file information and tracking each step
whether pass the parsing script, debug file

11). create a shell script to delete the files which expired for 3 days

12). add the time and component filter, the output files are sorted based on the type 

####5. Questions
Cultural Behavior Interview(this interview also has a shorter coding problem in it
Areas you will need to prepare in advance:
##### Information on your background as a developer
* Python, C
* Network, web application
* learn the distributed systems informaiton by myself

##### Projects you’re most proud of and that you’ve worked on
* Blogger, iParse 
* based on the Pyramid framework, 

##### How you cope with problems and conflicts at work (e.g. with team mates)
* Discussion in the team, point out the advantages and disadvantages between different plans 
* Check the customer requirement
* do the A/B testing to check the customer feedback 

##### Your biggest weaknesses and strengths
* Advantage:
   * focus on one thing, for example: blogger iparse, finished it in 3 months by myself 
   * a good teamworker and good communication skills, like to discussion with people and ask questions in their area, learn more
   * passionate about learning, furious on different things, and why, what, how
  
* Disadvantage:
    * "sometimes lack an attantion in details, While this is somewhat good in that it enables me to execute quickly, it also means that I can make careless mistakes. I have learned that I need to double or triple check important work before
submitting.", think deeply and also think broadly.
    * need to arrange the differnt work schedule 

##### Why you want to work at *** (from a developer point of view)
   * I like the company's culture: focus, passion, and fast, focused on building product and services that create a more open and connected world. 
   * I am very interested in the Facebook's products and keep following the news about Facebook, such as the 6-pack, F4, cold storage tech for pictures. But instead of just reading the tech blogs and understanding the open source technology, I wanna participate in the development. 
   * Facebook only has around 10,000 employees, but could reach and service for more than 1 billion people in the world, which is amazing. 

##### Why we need to hire you ?
* Culture: fit the company's culture
* I have the network background and also background about the webapplications 
* I have spent my spare time to keep learning the tech blogs in your company and have a deep understanding of products
* Recently, our component need to work with different teams simultaneously, I have been playing this intermediary role in my current position.

##### Ideas for new features (if you have any)
* could talk about sth learned from the system design preparation 

##### Hardest problem you’ve solved

##### Time you went above and beyond at work
###### What you want to work on at Facebook
* distributed systems develop
* many aspects: like typeahead, newsfeed, graph storage

##### What kind of position/role/team you are looking for
* Sth about develop the distributed systems, the scale system 

##### Difficulties/restrictions  about your current work place (e.g. from a technical point of view)
* current work is most about maintaince, little features, almost the same for each generation 
* Cisco is focus on the other generation produce rather than Nexus 7k till now

##### Why you want to work in a challenging environment
* Learn a lot of new thinks
* grow up every day 

#####Ideas on how to keep the quality of your work high while moving at a fast speed without a single QA
            
