const API="https://chaturbate.com/api/public/affiliates/onlinerooms/?wm=T2CSW&client_ip=request_ip";

async function initHome(){
  loadCountriesNav();
  loadRooms();
}

async function initPage(code,name){
  loadCountriesNav();
  document.title = name + " Live Cam Shows";
  loadRooms(code);
}

async function loadCountriesNav(){
  const res = await fetch('/data/countries.json');
  const countries = await res.json();
  const nav = document.getElementById("nav");
  nav.innerHTML = '<a href="/index.html">Home</a>';
  countries.forEach(c=>{
    nav.innerHTML += `<a href="/country/${c.slug}.html">${c.name}</a>`;
  });
}

async function loadRooms(filterCountry=null){
  const res = await fetch(API);
  const data = await res.json();
  const container = document.getElementById("rooms");
  container.innerHTML = "";
  data.results
    .filter(r=>!filterCountry||r.country===filterCountry)
    .sort((a,b)=>b.num_users-a.num_users)
    .forEach(room=>{
      container.innerHTML += `
      <div class="card">
        <a href="${room.url}?wm=T2CSW" target="_blank">
          <img src="${room.image_url}">
        </a>
        <div class="info">
          <b>${room.username}</b><br>
          🔥 ${room.num_users} watching
          <a class="btn" href="${room.url}?wm=T2CSW" target="_blank">🔴 JOIN LIVE SHOW</a>
        </div>
      </div>`;
    });
}
