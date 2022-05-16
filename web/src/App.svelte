<script lang="ts">
	import Autocomplete from "@smui-extra/autocomplete";
	import { Text } from "@smui/list";
	import CircularProgress from "@smui/circular-progress";
	import { onMount } from "svelte";
	import Fuse from 'fuse.js'

	let text = "";
	let playerName = undefined;
	let playerData;
	$:searcher = new Fuse(playerData);

	onMount(() => {
		getPlayers().then((data) => {
			console.log(data);
			playerData = data;
		});
	});

	function getData() {
		fetch("http://127.0.0.1:8000/player_data")
			.then((response) => response.json())
			.then((data) => console.log(data));
	}
 
	
	function getPlayers() {
		return fetch("http://127.0.0.1:8000/player_names").then((response) =>
			response.json()
		);
	}

	function handleSelect(event) {
		playerName = event.detail;
	}

	function handleClear() {
		playerName = undefined;
	}

	let value: string | undefined = undefined;

	let counter = 0;

	async function searchItems(input: string) {
		
		const result = searcher.search(input);
		console.log(result.slice(0,10));
		return result.slice(0,10);
	}
</script>

<main>
	<div>
		<Autocomplete
			search={searchItems}
			bind:value
			
			showMenuWithNoInput={false}
			label="Players"
		>
			<Text
				slot="loading"
				style="display: flex; width: 100%; justify-content: center; align-items: center;"
			>
				<CircularProgress
					style="height: 24px; width: 24px;"
					indeterminate
				/>
			</Text>
		</Autocomplete>
		<pre class="status">Selected: {value || ""}</pre>
	</div>
</main>


<!-- <script lang="ts">
import { onMount } from 'svelte';

	
	

	import Select from 'svelte-select';
	let text = "";
	let playerName = undefined;
	let playerData;

	onMount(()=>{
		getPlayers().then((data)=>{
			console.log(data);
			playerData = data;
		});

	})

	function getData() {
		fetch("http://127.0.0.1:8000/player_data")
			.then((response) => response.json())
			.then((data) => console.log(data));
	}

	function getPlayers() {
		return fetch("http://127.0.0.1:8000/player_names")
			.then((response) => response.json())
			
	}

	function handleSelect(event) {
		playerName = event.detail;
	}

	function handleClear() {
		playerName = undefined;
	}
</script>

<main>
	<h1>MLB PLAYERS X BROADWAY: THIS TIME IT'S TONAL</h1>
	<button on:click={getData}> Go! </button>
	<div>
		{text}
	</div>
	<div>
		<Autocomplete
		  search={searchItems}
		  bind:value
		  showMenuWithNoInput={false}
		  label="Fruit"
		>
		  <Text
			slot="loading"
			style="display: flex; width: 100%; justify-content: center; align-items: center;"
		  >
			<CircularProgress style="height: 24px; width: 24px;" indeterminate />
		  </Text>
		</Autocomplete>
		<pre class="status">Selected: {value || ''}</pre>
	  </div>

	<form>
		<label for='player'>Please choose a player to inspect</label>
		{#if playerData}
		<Select id='player' items = {playerData} on:select={handleSelect} on:clear={handleClear}></Select>
		{/if}

	</form>
	{#if playerName}
		<p1>Thank you for choosing {playerName.label} for your song inspection. Our sound engeneers will get back to you in the coming months with the resulting song.</p1>
	{/if}
</main>

<style>
	form{
		max-width: 400px;
		background: #afe4ee;
		padding: 20px;
		border-radius: 4px;
	}

	label {
		margin: 0 0 10px;
	}
</style>

 -->
