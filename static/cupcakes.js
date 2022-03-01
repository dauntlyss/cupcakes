$('.delete-cupcake').click(deleteCupcake)

async function deleteCupcake() {
    const id = $(this).data('id')
    await axios.delete(`/api/cupcakes/${id}`)
    $(this).parent().remove()
}

/** form handling for adding new cupcakes */
const BASE_URL ="http://localhost:500/api";
$("#new-cupcake-form").on("submit", async function (evt) {
    evt.preventDefault();

    let flavor = $("#form-flavor").val();
    let rating = $("#form-rating").val();
    let size = $("#form-size").val();
    let image = $("#form-image").val();

    const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
        flavor,
        rating,
        size,
        image
    });

    let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
    $("#cupcakes-list").append(newCupcake);
    $("#new-cupcake-form").trigger("reset");
});

// /** handle clicking delete button to delete cupcake */
// $("#cupcakes-list").on("click", ".delete-button", async function (evt) {
//     evt.preventDefault();
//     let $cupcake = $(evt.target).closest("div");
//     let cupcakeId = $cupcake.attr("data-cupcake-id");
//     await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
//     $cupcake.remove();
// });

// $(showInitialCupcakes);