// REF: https://kensu.atlassian.net/wiki/spaces/EN/pages/106431086/How-to+delete+entities+ingested+with+a+certain+token

async function sha256(message) {
  const msgBuffer = new TextEncoder().encode(message);
  const hashBuffer = await crypto.subtle.digest("SHA-256", msgBuffer);
  const hashArray = Array.from(new Uint8Array(hashBuffer));
  const hashHex = hashArray
    .map((b) => b.toString(16).padStart(2, "0"))
    .join("");
  return hashHex;
}

function del(authToken) {
  sha256(encodeURI("/services/v1/admin/graph/delete-entities-by-token"))
    .then((hash) => {
      console.log("hash: " + hash);
      return fetch("/services/v1/generate-token", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ hash: hash }),
      });
    })
    .then(function (res) {
      if (!res.ok) {
        return data.text().then(function (err) {
          throw new Error(err);
        });
      } else {
        return res.json();
      }
    })
    .then(function (data) {
      var csrf_token = data.data.token;
      console.log(
        "Requesting data deletion by token. It may be long, please wait..."
      );
      fetch("/services/v1/admin/graph/delete-entities-by-token", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-Token": csrf_token,
        },
        body: JSON.stringify({ token: authToken }),
      })
        .then(function (data) {
          if (!data.ok) {
            return data.text().then(function (err) {
              throw new Error(err);
            });
          } else {
            return data.json();
          }
        })
        .then(function (data) {
          console.log("Successfully deleted data by token", data);
        })
        .catch(function (error) {
          console.log("Failed to delete data by token: " + error);
        });
    })
    .catch(function (error) {
      console.log("Got error when retrieving CSRF token: " + error);
    });
}

function checkLockStatus() {
  sha256(
    encodeURI("/services/v1/admin/graph/check-entities-deletion-lock-status")
  )
    .then((hash) => {
      console.log("hash: " + hash);
      return fetch("/services/v1/generate-token", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ hash: hash }),
      });
    })
    .then(function (res) {
      if (!res.ok) {
        return res.text().then(function (err) {
          throw new Error(err);
        });
      } else {
        return res.json();
      }
    })
    .then(function (data) {
      var csrf_token = data.data.token;
      fetch("/services/v1/admin/graph/check-entities-deletion-lock-status", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-Token": csrf_token,
        },
      })
        .then(function (data) {
          if (!data.ok) {
            return data.text().then(function (err) {
              throw new Error(err);
            });
          } else {
            return data.json();
          }
        })
        .then(function (data) {
          console.log("Lockin status is:", data);
        })
        .catch(function (error) {
          console.log("Failed to check locking status: " + error);
        });
    });
}

function removeEnitiesDeletionLock() {
  sha256(encodeURI("/services/v1/admin/graph/rm-entities-deletion-lock"))
    .then((hash) => {
      console.log("hash: " + hash);
      return fetch("/services/v1/generate-token", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ hash: hash }),
      });
    })
    .then(function (res) {
      if (!res.ok) {
        return res.text().then(function (err) {
          throw new Error(err);
        });
      } else {
        return res.json();
      }
    })
    .then(function (data) {
      var csrf_token = data.data.token;
      fetch("/services/v1/admin/graph/rm-entities-deletion-lock", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRF-Token": csrf_token,
        },
      })
        .then(function (data) {
          if (!data.ok) {
            return data.text().then(function (err) {
              throw new Error(err);
            });
          } else {
            return data.json();
          }
        })
        .then(function (data) {
          console.log("Remove entities deletion lock:", data);
        })
        .catch(function (error) {
          console.log("Failed to remove entities deletion lock: " + error);
        });
    });
}
