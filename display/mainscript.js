/* Getting the html file elements */
let newuserdata = document.getElementById("userdata");
let users   //Database users in birthdata

async function getUsers() {
    let url = '../database/birthdatas.json';
    try {
        let res = await fetch(url);
        return await res.json();
    } catch (error) {
        console.log(error);
    }
}

async function showOldUserSection(){
    users = await getUsers();
    //Add options for dropdown
    let html = '';
    for (const [key, value] of Object.entries(users)) {
        let htmlSegment = `<option>${key}</option>
        `;

        html += htmlSegment;
      }
    let container = document.querySelector('#existingUserList');
    container.innerHTML = html;
    //Remove the input option section and display dropdown for old user list
    document.getElementById("c_inputoption").style.display = "none";
    document.getElementById("olduserdata").style.display = "block";
}

function showNewUserSection(){
    document.getElementById("c_inputoption").style.display = "none";
    document.getElementById("newuserdata").style.display = "block";
}







