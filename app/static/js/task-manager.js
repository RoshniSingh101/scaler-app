export class TaskManager {
    constructor(statusId) {
        this.statusEl = document.getElementById(statusId);
    }

    async startTask(videoId) {
        this.updateStatus("🚀 Sending...", "text-purple-400");
        const res = await fetch(`/process-video?video_id=${videoId}`, { method: 'POST' });
        const { task_id } = await res.json();
        this.poll(task_id);
    }

    async poll(taskId) {
        const interval = setInterval(async () => {
            const res = await fetch(`/task-status/${taskId}`);
            const data = await res.json();
            
            if (data.task_status === 'SUCCESS') {
                clearInterval(interval);
                this.updateStatus("✅ Done!", "text-green-400");
            }
        }, 2000);
    }

    updateStatus(msg, color) {
        this.statusEl.innerText = msg;
        this.statusEl.className = `mt-4 text-xs text-center ${color}`;
    }
}