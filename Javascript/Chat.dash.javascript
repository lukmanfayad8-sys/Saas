const taskForm = document.getElementById("taskForm");
const taskName = document.getElementById("taskName");
const taskStatus = document.getElementById("taskStatus");
const taskTable = document.getElementById("taskTable");

taskForm.addEventListener("submit", function (e) {
  e.preventDefault();

  const name = taskName.value;
  const status = taskStatus.value;

  // Create row
  const row = document.createElement("tr");

  // Task cell
  const taskCell = document.createElement("td");
  taskCell.textContent = name;

  // Status cell
  const statusCell = document.createElement("td");
  statusCell.textContent = status;

  if (status === "Done") {
    statusCell.classList.add("status-done");
  } else {
    statusCell.classList.add("status-pending");
  }

  row.appendChild(taskCell);
  row.appendChild(statusCell);
  taskTable.appendChild(row);

  // Clear form
  taskForm.reset();
});