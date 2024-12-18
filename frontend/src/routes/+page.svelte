<script>
    import { onMount } from 'svelte';
    import Cookies from 'js-cookie';
    
    let todo = '';
    let todoList = [];
    let loading = false;
    
    // Function to save todos to cookies
    function saveTodosToCookies() {
        Cookies.set('todoList', JSON.stringify(todoList), { expires: 100 }); // Expires in 7 days
    }
    
    // Function to load todos from cookies
    function loadTodosFromCookies() {
        const savedTodos = Cookies.get('todoList');
        return savedTodos ? JSON.parse(savedTodos) : [];
    }
    
    async function AddTask() {
        if (!todo.trim()) return;
        
        loading = true;
        try {
            todoList = [...todoList, todo];
            saveTodosToCookies();
            todo = '';
        } catch (error) {
            console.error('Error:', error);
        } finally {
            loading = false;
        }
    }

    async function RemoveTask(item) {
        loading = true;
        try {
            todoList = todoList.filter(todo => todo !== item);
            saveTodosToCookies();
        } catch (error) {
            console.error("error removing task " + error)
        } finally {
            loading = false;
        }
    }

    onMount(() => {
        loading = true;
        try {
            todoList = loadTodosFromCookies();
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
            <li>
                {item}
                <button on:click={() => RemoveTask(item)} disabled={loading}>
                    {loading ? 'Removing...' : 'Remove'}
                </button>
            </li>
        {/each}
    </ul>
{:else}
    <p>No tasks yet</p>
{/if}
