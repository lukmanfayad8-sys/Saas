
//default display
document.addEventListener("DOMContentLoaded",()=>{
   card.style.display='block';
  recent.style.display='block';
   team_form.style.display='none';
  team_table.style.display='none';
   task_section_form.style.display='none';
  task_table.style.display='none';
  account_settings .style.display='none';
team_management_settings.style.display='none';
notification_settings.style.display='none';
billing_settings.style.display='none';
savebtn.style.display='none';
});


// side bar toggle
//slide-out
const open = document.getElementById('open');
const side_nav =document.getElementById('sideNav');
open.addEventListener('click',()=>{
 side_nav.style.display = 'flex'
});
// slide-in
const close = document.getElementById('close');
close.addEventListener('click',()=>{
 side_nav.style.display = 'none';
});

//dashboard navi btn
const dashboardbtn = document.getElementById('dashboard');
//visible on Dashboard but not on task board
const card = document.getElementById('status');
const recent =document.getElementById('table_3');
//not visible on dash board

dashboardbtn.addEventListener('click', (dash)=>{
  card.style.display='block';
  recent.style.display='block';
   team_form.style.display='none';
  team_table.style.display='none';
   task_section_form.style.display='none';
  task_table.style.display='none';
  account_settings .style.display='none';
team_management_settings.style.display='none';
notification_settings.style.display='none';
billing_settings.style.display='none';
savebtn.style.display='none';
});


//task navi btn
const taskbtn = document.getElementById('taskbtn');
//display in task table
const task_section_form = document.getElementById('taskForm');
const task_table = document.getElementById('table_4');
document.addEventListener("DOMContentLoaded",()=>{  
taskbtn.addEventListener('click',()=>{
  task_section_form.style.display='block';
  task_table.style.display='block';
   team_form.style.display='none';
  team_table.style.display='none';
  card.style.display='none';
  recent.style.display='none';
  savebtn.style.display='none';
 });
});
//team navi btn
const teambtn = document.getElementById('teambtn');
//display in task table

const team_table = document.getElementById('team');

teambtn.addEventListener('click',()=>{
  team_form.style.display='block';
  team_table.style.display='block';
   task_section_form.style.display='none';
  task_table.style.display='none';
  card.style.display='none';
  recent.style.display='none';
  account_settings .style.display='none';
team_management_settings.style.display='none';
notification_settings.style.display='none';
billing_settings.style.display='none';
savebtn.style.display ='none';
});

//Settings navibtn
const settingBtn = document.getElementById('Settings');
const savebtn = document.getElementById('Savebtn');
const account_settings = document.getElementById('Settings-accounts');
const team_management_settings = document.getElementById('Settings-team-Management');
const notification_settings = document.getElementById('Settings-notifications');
const billing_settings = document.getElementById('Settings-billing');

settingBtn.addEventListener('click',()=>{
account_settings .style.display='block';
team_management_settings.style.display='block';
notification_settings.style.display='block';
billing_settings.style.display='block';
card.style.display='none';
  recent.style.display='none';
   team_form.style.display='none';
  team_table.style.display='none';
  task_section_form.style.display='none';
  task_table.style.display='none';
});

//

const task = document.getElementById('Newtaskbtn');
const task_Name = document.getElementById('taskName');
const task_Priority = document.getElementById('task_Priority');
const task_body= document.getElementById('task-body')
const members = document.getElementById('task_Members');
const Description = document.getElementById('descriptions');

task.addEventListener('submit',function (task_btn){
  task_btn.preventDefault();
  const taskName = task_Name.value; 
  const taskPriority = task_Priority.value;
  const Members = members.value;
  const Des_cription = Description.value
  const row = document.createElement('tr');

  const Assigned_to_a_user ={
    taskName,
    taskPriority,
    Members,
    Des_cription
  };
  row.innerHTML = `
  <td>${ taskName}</td>
  <td>${ taskPriority}</td>
  <td>${ Members}</td>
   <td>${ Des_cription}</td>
  <td></td>`
  task_body.appendChild(row);

  
  localStorage.setItem(Assigned_to_a_user,JSON.stringify(Assigned_to_a_user));

  task_btn.target.reset();
});



// For add Team table to display function
const team = document.getElementById('Addteambtn');
const team_form = document.getElementById('teamForm');
const Name = document.getElementById('teamName');
const email = document.getElementById('teamMail');
const tel = document.getElementById('teamTel');
const teamTable = document.getElementById('teamTable');
const tbody = document.getElementById('innertable');

team.addEventListener('submit',function (add_team) {
  add_team.preventDefault();
 const tbody = document.getElementById('innertable')
  const team_Name = Name.value; 
  const team_Mail = email.value;
  const team_Tel = tel.value;

  
  const admin ={
  team_Name,
  team_Mail,
  team_Tel,
  } 

  const row = document.createElement('tr');
  row.innerHTML = `
  <td>${team_Name}</td>
  <td>${team_Mail}</td>
  <td>${team_Tel}</td>
  <td> </td>`
 tbody.appendChild(row)
   
  
  localStorage.setItem(admin, JSON.stringify(admin));
        

  add_team.target.reset();
});



function del () {
  let teams = JSON.parse(localStorage.getItem(admin)) || [];
    teams = teams.filter(team => team.Id !== Id);
    localStorage.setItem(admin,JSON.stringify(teams)),
    renderTeams();
}