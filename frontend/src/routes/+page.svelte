<script>
    import { onMount } from 'svelte';
    
    let todo = '';
    let todoList = [];
    let loading = false;
    
    const API_URL = 'http://127.0.0.1:5000';  // Define base URL once
    
    async function AddTask() {
        if (!todo.trim()) return;
        
        loading = true;
        try {
            const response = await fetch(`${API_URL}/add/${encodeURIComponent(todo)}`, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            todoList = data.todoList;
            todo = '';
        } catch (error) {
            console.error('Error:', error);
        } finally {
            loading = false;
        }
    }

    onMount(async () => {
        loading = true;
        try {
            const response = await fetch(`${API_URL}/show`, {
                method: 'GET',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                }
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            const data = await response.json();
            todoList = data.todoList;
        } catch (error) {
            console.error('Error loading initial data:', error);
        } finally {
            loading = false;
        }
    });
</script>

<div>
    <input 
        type="text" 
        bind:value={todo}
        placeholder="Enter a task"
        disabled={loading}
    />
    <button on:click={AddTask} disabled={loading}>
        {loading ? 'Adding...' : 'Add Task'}
    </button>
</div>

{#if loading}
    <p>Loading...</p>
{:else if todoList && todoList.length > 0}
    <ul>
        {#each todoList as item}
            <li>{item}</li>
        {/each}
    </ul>
{:else}
    <p>No tasks yet</p>
{/if}
