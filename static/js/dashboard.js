fetch("/dashboard/overview")
  .then(res => res.json())
  .then(data => {
    document.getElementById("data").innerHTML =
      JSON.stringify(data, null, 2);
  });
