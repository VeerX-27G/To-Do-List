// Base URL of our API (same origin, so relative paths work fine)
const API_URL = "/todos/";

const form = document.getElementById("todo-form");
const input = document.getElementById("title-input");
const list = document.getElementById("todo-list");

// Fetch all todos from the backend and render them
async function loadTodos() {
  const res = await fetch(API_URL);
  const todos = await res.json();

  list.innerHTML = ""; // clear current list

  todos.forEach(todo => {
    const li = document.createElement("li");
    if (todo.completed)
        li.classList.add("completed");

    li.innerHTML = `
      <span>${todo.title}</span>
      <div class="actions">
        <button class="toggle-btn" onclick="toggleTodo(${todo.id}, ${!todo.completed}, '${todo.title.replace(/'/g, "\\'")}')">
          ${todo.completed ? "Undo" : "Done"}
        </button>
        <button onclick="deleteTodo(${todo.id})">Delete</button>
      </div>
    `;
    list.appendChild(li);
  });
}

// Handle form submit -> create a new todo
form.addEventListener("submit", async (e) => {
  e.preventDefault(); // stop page from reloading
  const title = input.value.trim();
  if (!title)
      return;

  await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(
        {
            title,
            completed: false
        }
    )
  });

  input.value = "";
  loadTodos(); // refresh list
});

// Toggle a todo's completed status (uses PUT to update it)
async function toggleTodo(id, newStatus, title) {
  await fetch(`${API_URL}${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(
        {
            title,
            completed: newStatus
        })
  });
  loadTodos();
}

// Delete a todo
async function deleteTodo(id) {
  await fetch(`${API_URL}${id}`, { method: "DELETE" });
  loadTodos();
}

// Load todos when the page first opens
loadTodos();