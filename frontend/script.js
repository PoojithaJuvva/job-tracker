const API = "http://127.0.0.1:5000";

// ADD
async function addJob() {
    let company = document.getElementById("company").value;
    let role = document.getElementById("role").value;
    let status = document.getElementById("status").value;

    await fetch(API + "/add_job", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({company, role, status})
    });

    loadJobs();
}

// LOAD
async function loadJobs() {
    let res = await fetch(API + "/get_jobs");
    let data = await res.json();

    let list = document.getElementById("jobList");
    list.innerHTML = "";

    data.forEach(job => {
        let div = document.createElement("div");
        div.className = "job-card";

        let statusClass = "";

        if (job.status === "Applied") statusClass = "applied";
        else if (job.status === "Interview") statusClass = "interview";
        else if (job.status === "Rejected") statusClass = "rejected";

        div.innerHTML = `
            <b>${job.company}</b> - ${job.role}
            <span class="status ${statusClass}">${job.status}</span>
            <br><br>

            <select onchange="updateJob(${job.id}, this.value)">
                <option ${job.status==='Applied'?'selected':''}>Applied</option>
                <option ${job.status==='Interview'?'selected':''}>Interview</option>
                <option ${job.status==='Rejected'?'selected':''}>Rejected</option>
            </select>

            <button class="delete-btn" onclick="deleteJob(${job.id})">Delete</button>
        `;

        list.appendChild(div);
    });
}

// UPDATE
async function updateJob(id, status) {
    await fetch(API + "/update_job/" + id, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({status})
    });

    loadJobs();
}

// DELETE
async function deleteJob(id) {
    await fetch(API + "/delete_job/" + id, {
        method: "DELETE"
    });

    loadJobs();
}

// AUTO LOAD
loadJobs();