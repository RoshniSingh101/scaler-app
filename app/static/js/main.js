import { TaskManager } from './task-manager.js';

// initialize the task manager for the specific status element
const taskManager = new TaskManager('taskStatus');

const taskBtn = document.getElementById('taskBtn');
if (taskBtn) {
    taskBtn.addEventListener('click', () => {
        taskManager.startTask('fancy_ui_test');
    });
}