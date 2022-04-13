import React from "react";
// We would like to use a modal (small window) to show details of a task.
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      activeRating: this.props.activeRating,
    };
  }

  handleChange = (event) => {
    let { name, value } = event.target;
    if (event.target.type === "checkbox") {
      value = event.target.checked;
    }
    const activeRating = { ...this.state.activeRating, [name]: value };
    //console.log(activeRating)
    this.setState({ activeRating });
  };
  render() {
    // The modal has three properties: toggle, onSave, and activeItem.
    // We have already defined activeItem above.
    // See App.js on how toggle, onSave, and activeItem are being used.
    const { toggle, onSave } = this.props;
    return (
      // isOpen={true} is a Boolean describing if the modal should be shown or not,
      // i.e., in our case, what should happen if the modal is open.
      // Open the modal on toggling/clicking. See the toggle function in App.js
      // below.
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}> New Rating </ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="rating">Rating</Label>
              <Input
                type="number"
                name="rating"
                value={this.state.activeRating.rating}
                // "this" refers to the current event. If there is a change,
                // it will be passed to the handleChange function above.
                onChange={this.handleChange}
                placeholder="Enter Song Rating"
              />
            </FormGroup>
            <FormGroup>
              <Label for="user">Username</Label>
              <Input
                type="text"
                name="user"
                value={this.state.activeRating.user}
                // "this" refers to the current event. If there is a change,
                // it will be passed to the handleChange function above.
                onChange={this.handleChange}
                placeholder="Enter Username"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button color="success" onClick={() => onSave(this.state.activeRating)}>
            Save
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}