import React from "react";
// Import the CustomModal that we created in Modal.js.
import Modal from "./components/Modal";
import axios from "axios";

class App extends React.Component {
  // Here comes our constructor.
  constructor(props) {
    super(props);
    this.state = {
      activeSong: {
        name: "",
        artist: "",
        rating: 0,
      },
      songList: [],
      ratingList: [],
    };
  }
  componentDidMount() {
    this.refreshSongList();
  }

  refreshSongList = () => {
    // We are using the axios library for making HTTP requests.
    // Here is a GET request to our api/todos path.
    // If it succeeds, we set the todoList to the resolved data.
    // Otherwise, we catch the error and print it to the console (rejected data).
    // We are using async calls here. Please refer to the JavaScript
    // tutorial for how they work.
    axios
      .get("http://localhost:8000/api/song/")
      // To change a value in the `state` object for rendering, use `setState()`.
      // Here we get all todoList data. Each resolve (res) object has a data field.
      .then((res) => this.setState({ songList: res.data }))
      .catch((err) => console.log(err));
    console.log('hello')
  };

  refreshRatingList = () => {
      axios
      .get("http://localhost:8000/api/rating/")
      // To change a value in the `state` object for rendering, use `setState()`.
      // Here we get all todoList data. Each resolve (res) object has a data field.
      .then((res) => this.setState({ ratingList: res.data }))
      .catch((err) => console.log(err));
    console.log('rating refresh')
    };



  renderSongs = () => {
    // Destructuring assignment that assigns viewCompleted = this.state.viewCompleted
    // const { viewCompleted } = this.state;
    // filter is a callback function that returns the elements of an array
    // meeting a particular condition; here all items that are viewCompleted.
    const newItems = this.state.songList;
    // The items are then mapped to their UI elements based on their id, i.e.,
    // item.id, item.description, and item.title.
    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span /////////////////
          className={`todo-title mr-2 `}
          //</li>this.state.viewCompleted ? "completed-todo" : ""
        //}
          title={item.id}
        >
          {item.name} - {item.artist}
        </span>
        {/* UI for editing and deleting items and their respective events. */}
        <span>
          <button
            // If the user clicks the Edit button, call the editItem function.
            onClick={() => this.editItem(item)}
            className="btn btn-secondary mr-2"
          >
            {" "}
            Edit{" "}
          </button>
          <button
            // If the user clicks the Delete button, call the handleDelete function.
            onClick={() => this.handleDelete(item)}
            className="btn btn-danger"
          >
            Delete{" "}
          </button>
        </span>
      </li>
    ));
  };
  toggle = () => {
    // We have a modal view below in the render() function.
    // Upon toggle, set the modal to false, i.e., do not show the modal.
    this.setState({ modal: !this.state.modal });
  };
  // Another custom function.

  handleSubmit = (item) => {
    this.toggle();
    // If the item already exists in our database, i.e., we have an id for our
    // item, use a PUT request to modify it.
    if (item.id) {
      axios
        // Note that we are using backticks here instead of double quotes.
        // Backticks are useful because they allow us to use dynamic variables,
        // i.e., the item.id in this case. You can use this technique also
        // for authentication tokens.
        .put(`http://localhost:8000/api/song/${item.id}/`, item)
        .then((res) => this.refreshSongList());
      return;
    }
    axios
      .post("http://localhost:8000/api/song/", item)
      .then((res) => this.refreshSongList());
  };
  handleDelete = (item) => {
    axios
      .delete(`http://localhost:8000/api/song/${item.id}`)
      .then((res) => this.refreshSongList());
  };
  createItem = () => {
    const item = { name:"", artist:"",rating:0};//, description: "", completed: false };
    this.setState({ activeSong: item, modal: !this.state.modal });
  };
  // Another custom function.
  // If the use triggers an editItem event.
  editItem = (item) => {
    this.setState({ activeSong: item, modal: !this.state.modal });
  };

  // The `render()` method is the only required method in a class component.
  // When called, it will render the page. You do not have to specifically
  // call render() in your component. Rather, the stub code with the
  // ReactDOM.render(...) in your index.js will do that for you.
  render() {
    return (
      <main className="content">
        <h1 className="text-white text-uppercase text-center my-4">Song Rater</h1>
        <div className="row ">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="">
                {/* If the user clicks the Add task button, call the createItem function. */}
                <button onClick={this.createItem} className="btn btn-primary">
                  Add Song
                </button>
              </div>
              {/* {this.renderTabList()}  */}
              <ul className="list-group list-group-flush">
                {this.renderSongs()}
              </ul>
            </div>
          </div>
        </div>
        {/* If the modal state is true, show the modal component. */}
        {this.state.modal ? (
          <Modal
            activeSong={this.state.activeSong}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}

// Export our App so that it can be rendered in index.js, where it is imported.
export default App;
